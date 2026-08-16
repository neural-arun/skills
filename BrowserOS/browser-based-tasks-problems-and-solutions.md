# Browser-Based Tasks: Problems Faced & How I Solved Them

A detailed log of the issues encountered while doing browser-heavy tasks via BrowserOS
MCP — going to GitHub, posting on X (Twitter), and reading LinkedIn — and the exact
solutions that worked.

---

## Table of Contents

- [1. GitHub: Finding the "Latest Commit"](#1-github-finding-the-latest-commit)
- [2. X (Twitter): The Composer Is a War Zone](#2-x-twitter-the-composer-is-a-war-zone)
- [3. X (Twitter): Character Count Rules](#3-x-twitter-character-count-rules)
- [4. X (Twitter): Posting Threads (Multi-Tweet)](#4-x-twitter-posting-threads-multi-tweet)
- [5. Tab Ownership & Session Rules](#5-tab-ownership--session-rules)
- [6. LinkedIn: Reading the Activity Feed](#6-linkedin-reading-the-activity-feed)
- [7. General Lessons (The "How to Do It Right" Cheat Sheet)](#7-general-lessons)

---

## 1. GitHub: Finding the "Latest Commit"

### Problem
The user asked for a tweet about the **latest GitHub commit**. Simple, right? No.

- The GitHub profile page (`github.com/neural-arun`) showed a contribution graph with
  activity, but clicking into the **default repo view showed "No commits"** for the
  `skills` repo.
- The repo's default branch on GitHub was `main` (empty), but the real work lived on
  a branch called **`master`**. The local repo and the remote had different branch
  names.
- Mistake made: I initially tweeted about a **different repo** (`study_helper_bot`) that
  had recent commits but was **not** the latest push. The user corrected me.

### Solution
1. **Ask the local machine.** Ran `git log --all` in `/home/arun/projects/skills` to
   see actual commit hashes, dates, and messages the remote may hide.
2. **Cross-referenced with remote.** Checked which branch the remote actually used
   (`git branch`, `git remote -v`).
3. **Navigated to the real URL.** The GitHub web UI default view (branch `main`) was
   misleading — I went to `github.com/neural-arun/skills/commits/master` directly to
   see the real commit history.
4. **Verified dates.** Confirmed the latest commit (`f56e6c5` "made some more youtube
   notes", dated 2026-08-16, today) matched the contribution graph before choosing it
   as the tweet subject.
5. **Chose the right repo.** Only after this verification did I pick the `skills`
   repo (the actual latest push) over `study_helper_bot`.

**Lesson:** Never trust the GitHub default branch view. Always check the local git
history, the actual branch name, and confirm the date matches before picking a
"latest commit."

---

## 2. X (Twitter): The Composer Is a War Zone

The `x.com/compose/post` text box is a contenteditable React/Lexical editor. It does
**not** behave like a normal `<textarea>`. These were the key battles:

### 2.1 Too Many Blank Lines (Character Waste)

**Problem**
The `fill` action inserted content with a run of blank lines (`\n\n\n\n\n`).
Every blank line eats characters, and I was pushing against the 280 limit. The final
tweet was 49 chars over.

**Solution**
Used JavaScript in the page context to clean the box:
```js
document.execCommand('selectAll');
document.execCommand('delete');
```
This reliably clears the composer without fighting React's state.

### 2.2 Text Got Appended / Concatenated Instead of Replaced

**Problem**
Filling again after some content existed **appended** the new text to the old rather
than replacing it (or kept duplicated fragments). A second `fill` to fix earlier text
made it worse.

**Solution**
- NEVER `fill` twice into the same composer. If the content is wrong, either
  `selectAll + delete` first (see above) or **navigate away and open a fresh
  `x.com/compose/post`** — always start from a clean editor.

### 2.3 Markdown Bold `**` Printed Literally

**Problem**
The tweet-crafting skill (and my drafts) used `**bold**` markdown. X doesn't render
markdown — the asterisks would have posted as literal `**` characters, looking broken
and wasting characters.

**Solution**
Stripped all `**` from the tweet body before composing. On X, emphasis is done with
all-caps or emoji, never markdown.

### 2.4 Post Button Stayed Disabled

**Problem**
After JavaScript-based text manipulation, the "Post" button remained greyed out.
React's state machine didn't know the textbox changed (the `input` event was never
fired by our JS edits).

**Solution**
Fire the event React listens for, after the text write:
```js
document.execCommand('insertText', false, 'YOUR TWEET TEXT');
dispatchEvent(new InputEvent('input', { bubbles: true }));
```
`insertText` (instead of setting `innerText` directly) makes the editor generate a
proper input event, and the extra dispatched `InputEvent('input')` wakes up React's
state → the button enables. Setting `.innerText` directly returns an empty string and
did **not** enable the button.

### 2.5 Refreshing / Resetting Stale State

**Problem**
After a failed fill, the composer held garbage and even the fresh-text fix above
didn't fully settle.

**Solution**
When in doubt, **reload the page** (`browseros_navigate` reload) or open a brand-new
`x.com/compose/post` tab. A corrupt composer is cheaper to replace than to repair.

---

## 3. X (Twitter): Character Count Rules

### Problem
Tweets were exceeding 280 and I didn't understand why counting was off.

### Facts discovered (verified against X's own counter)
- Standard **letters, numbers, spaces, punctuation count as 1 char** each.
- **Every emoji counts as 2 characters** — even a single unicode emoji.
- **`https://` URLs count as exactly 23 characters** (X's link wrapper), regardless of
  length.
- A **bare domain** like `github.com/neural-arun/skills` counts its full length
  (it isn't auto-detected as a link), so it's cheaper/hazardous to count wrong.

### Solution
- Count text with `text.length` plus **2 per emoji**.
- For links, assume **23 chars** whenever you use a full `https://` URL.
- Rewrote the final tweet (267 chars) under the 280 limit and **verified against X's
  own live counter** in the composer before posting.

**Lesson:** Emojis ×2, https-links = 23. Always verify with X's live counter, not just
local math.

---

## 4. X (Twitter): Posting Threads (Multi-Tweet)

### Problem
The LinkedIn task required posting a **5-tweet thread**. I initially tried composing
tweets one-by-one in the main composer, which is wrong for threads.

### Solution
1. Opened fresh `x.com/compose/post`.
2. Wrote tweet 1, then clicked the **"Add post"** button to append each subsequent
   tweet box (each box is a separate composer in one buffer).
3. Kept **every individual tweet under 280** (they were 206/213/221/222/232 chars).
4. Clicked **"Post all"** to publish the whole thread at once (instead of Post, which
   only posts the single first tweet).
5. Verified the result on `x.com/Neural_Arun/status/<id>` — all 5 rendered in
   sequence with correct numbers.

**Lesson:** Threads = "Add post" to build, "Post all" to publish. Never "Post" for a
multi-tweet thread.

---

## 5. Tab Ownership & Session Rules

### Problem
BrowserOS windows/pages are **per-agent and per-user**. On first attempt I tried to
act on a tab that belonged to the user (page 10) — the tool rejected it with a
"not owned by this agent" error. Acting on tabs you don't own fails cleanly.

### Solution
- Opened my **own tab** with `tabs action="new"` pointing at the URL I needed, and
  did all work there.
- Tracked which page IDs were mine (composer on my page 21, LinkedIn activity on my
  page 24) and reused them instead of opening duplicates each time.

**Lesson:** If a page isn't yours, open your own copy with `tabs new` at the same URL
and leave the original untouched.

---

## 6. LinkedIn: Reading the Activity Feed

### Problem
- The LinkedIn activity feed (`/in/<username>/recent-activity/all/`) markup is huge.
- A full `read`/snapshot hit **truncation limits** and the tool saved the overflow to a
  separate file.
- I needed specific signal — the **titles/heads of the user's recent posts** ("Week 4
  → done", "Finished Week 3 of AI Engineering Core by Ed Donner", etc.) and their
  order (most recent = Week 4).

### Solution
1. Navigated directly to `.../recent-activity/all/` (the dedicated activity URL) rather
   than scrolling the profile overview.
2. Instead of dumping the whole page, used **targeted `browseros_grep` over `content`**
   with patterns for the post headers to pull exactly the lines I needed:
   - `grep over="content" pattern="Week"` → caught every week's post title.
   - Additional patterns (`Ed Donner`, `Clinical Document Assistant`, `AI Twin`) to
     confirm the set of topics.
3. Used the returned relative lines + their order to reconstruct the thread content
   (most recent on top) without ever opening the truncated file.

**Lesson:** For content-heavy sites, **grep beats full read**. Pull only the regex
lines you need instead of paying for a 5000-char dump or chasing a saved-truncated file.

---

## 7. General Lessons (The "How to Do It Right" Cheat Sheet)

1. **Verify before you tweet.** Confirm which commit/repo/post is the actual latest
   (local `git log` + date check) before choosing the subject. I posted a wrong-repo
   tweet once because I skipped this.
2. **Never double-`fill` a composer.** If content is wrong, `selectAll+delete` or open a
   fresh `x.com/compose/post`. Starting clean is faster than repairing React state.
3. **Count characters the X way:** 1/char text, **2 per emoji**, **23 per `https://`
   link**. Verify with X's live counter.
4. **Threads:** "Add post" to build boxes, "Post all" to publish, every tweet < 280.
5. **Own only your tabs.** Never touch user/other-agent tabs; open your own copy.
6. **Use `grep` for big pages.** LinkedIn/snapshots truncate; targeted regex pulls beat
   full reads.
7. **Wake up React with real events.** After JS text edits, dispatch
   `new InputEvent('input', { bubbles: true })` so buttons enable.
8. **Don't fight a broken composer — reload it.** A reloaded page is a fresh state.
9. **Stripped markdown (`**bold\*\*`)** for X — it posts literally otherwise.
10. **Keep posting volume low and content unique.** Using a real logged-in browser with
    low frequency and human-sounding posts = low block risk. Volume + verbatim copies +
    link spam are what get accounts flagged.