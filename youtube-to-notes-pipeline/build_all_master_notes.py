import os
import glob
import json
import re

WORK_DIR = "./outputs/Backend_engineering_work"
DEST_DIR = "./outputs/Backend_engineering_notes"
MANIFEST_PATH = os.path.join(WORK_DIR, "manifest.json")

# Map of topic-native headers, diagrams, and AI Systems Engineering takeaways for all 23 lessons
LESSON_METADATA = {
    "01_Roadmap_for_backend_from_first_principles": {
        "title": "1. Roadmap for Backend from First Principles",
        "diagram_1": """```mermaid
mindmap
  root((Backend Architecture Roadmap))
    Protocol Layer
      TCP/IP Sockets
      HTTP 1.1 / HTTP 2 / gRPC
      TLS Termination
    Compute & Logic
      Stateless Process Execution
      Middlewares & Request Context
      Controller Services Repo Pattern
    Data & Persistence
      Relational DBs Postgres ACID
      NoSQL & Vector DBs Chroma/Pinecone
      Caching Strategies Redis
    Distributed Systems
      Message Queues RabbitMQ/Celery
      Scaling & Load Balancing
      Fault Tolerance & Observability
```""",
        "diagram_2": """```mermaid
graph TD
    Client[Client / AI Agent / Front-end] -->|HTTP Request / gRPC| Gateway[Reverse Proxy / Nginx / Gateway]
    Gateway -->|SSL Termination & Routing| AppServer[FastAPI / Web Server]
    AppServer -->|Auth Middleware| Controller[Request Controller]
    Controller -->|Business Logic| Service[Domain Service Layer]
    Service -->|Query Execution| DB[(PostgreSQL Primary)]
    Service -->|Cache Lookup| Redis[(Redis Cache)]
    Service -->|Async Job Dispatch| Queue[(Celery / Message Queue)]
```"""
    },
    "02_Walk_the_path_of_a_true_backend_engineer": {
        "title": "2. Walk the Path of a True Backend Engineer",
        "diagram_1": """```mermaid
mindmap
  root((Backend Mindset & Mental Models))
    First Principles Thinking
      Understanding System Boundaries
      Hardware & OS Constraints
      Network Latency vs Memory Access
    Engineering Rigor
      Failure Domain Isolation
      Idempotency by Design
      Trade-off Analysis Memory vs CPU
    AI Systems Mappings
      Deterministic Execution in Non-Deterministic AI
      Structured Tool Calling via MCP
      Reliable State Machines for Agents
```""",
        "diagram_2": """```mermaid
graph LR
    A[Raw Prompt / Request] --> B{Validation & Schema Check}
    B -->|Valid| C[Agent Execution Pipeline]
    B -->|Invalid| D[Immediate Early Rejection 400]
    C --> E[State Machine Evaluation]
    E --> F[Database Transaction]
    E --> G[External MCP Tool Call]
```"""
    },
    "03_What_is_a_Backend_how_do_they_work_and_why_do_we_need_them": {
        "title": "3. What is a Backend, How Do They Work and Why Do We Need Them?",
        "diagram_1": """```mermaid
mindmap
  root((Backend Fundamentals))
    Core Responsibilities
      Business Logic Enforcement
      Data Persistence & Integrity
      Security & Access Control
    State Management
      Stateless API Layer
      Stateful Storage Engines
      Distributed Session Locks
    AI System Connections
      Orchestrating LLM Context Windows
      Managing RAG Embeddings & Metadata
      Persisting Conversation Trajectories
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    autonumber
    Client->>Backend: POST /v1/agent/run (Payload)
    Backend->>AuthMiddleware: Validate Token & Scopes
    AuthMiddleware-->>Backend: Token Verified (User Context)
    Backend->>Database: Fetch User State & Session
    Database-->>Backend: User State Record
    Backend->>LLM/MCP Tool: Execute Tool & Process Request
    LLM/MCP Tool-->>Backend: Tool Response
    Backend->>Database: Commit Transaction / Save State
    Backend-->>Client: 200 OK (Execution Result)
```"""
    },
    "04_Benefits_of_learning_backend_engineering_from_first_principles": {
        "title": "4. Benefits of Learning Backend Engineering from First Principles",
        "diagram_1": """```mermaid
mindmap
  root((First-Principles Advantage))
    Framework Independence
      Understanding Under-the-Hood I/O
      Socket Level Awareness
      Memory Allocation vs GC Overhead
    Debugging Mastery
      Tracing Packet Loss & Connection Timeouts
      Diagnosing Database Lock Contention
      Profiling Latency Bottlenecks
    AI Engineering Relevance
      Building Low-Latency Vector Search
      Optimizing Parallel Agent Tool Execution
      Designing Robust Retry / Fallback Pipelines
```""",
        "diagram_2": """```mermaid
graph TD
    Sub[High-Level Framework Abstraction] -->|Hides Mechanisms| Fail[Mystery Failures & Performance Wall]
    FP[First Principles Awareness] -->|Understands Sockets, Memory, Locks| Solv[Predictable Scaling & Instant Diagnostics]
    Solv --> RAG[Low Latency RAG Pipelines]
    Solv --> Agent[High Throughput Agent Swarms]
```"""
    },
    "05_Understanding_HTTP_for_backend_engineers_where_it_all_starts": {
        "title": "5. Understanding HTTP for Backend Engineers",
        "diagram_1": """```mermaid
mindmap
  root((HTTP Protocol Deep Dive))
    Protocol Evolution
      HTTP/1.1 Head-of-Line Blocking & Keep-Alive
      HTTP/2 Binary Streams & Multiplexing
      HTTP/3 QUIC & UDP Transport
    Request Structure
      Method GET POST PUT DELETE
      Header Parsing Content-Type Authorization
      Payload Body Chunked vs Fixed Length
    Response Handling
      Status Codes 2xx 4xx 5xx
      Server-Sent Events (SSE) Streaming
      Connection Pooling & Socket Reuse
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    participant Client
    participant Server
    Client->>Server: TCP 3-Way Handshake (SYN, SYN-ACK, ACK)
    Client->>Server: TLS Handshake (Client Hello, Server Hello, Key Exchange)
    Client->>Server: POST /v1/chat/completions (Stream: true)
    Server-->>Client: HTTP/1.1 200 OK (Transfer-Encoding: chunked / text/event-stream)
    Server-->>Client: data: {"chunk": "Hello"}
    Server-->>Client: data: {"chunk": " World"}
    Server-->>Client: data: [DONE]
```"""
    },
    "06_What_is_Routing_in_Backend_How_Requests_Find_Their_Way_Home": {
        "title": "6. What is Routing in Backend? How Requests Find Their Way Home",
        "diagram_1": """```mermaid
mindmap
  root((Routing Architecture))
    Router Internals
      Trie / Radix Tree Route Matching
      Regex vs Exact Path Matching
      URL Parameter Parsing
    Gateway & Proxy Routing
      Host-Based Routing
      Path-Based Routing
      Load Balancer Algorithm Round Robin / Least Conn
    AI Gateway Routing
      Routing Prompts by Complexity
      Model Fallback Routing GPT4 -> Claude -> Local
      Rate-Limited Queue Routing
```""",
        "diagram_2": """```mermaid
graph TD
    Req[Incoming Request /api/v1/tools/search] --> Router{Radix Tree Lookup}
    Router -->|/api/v1/tools| ToolGroup[Tool Sub-Router]
    ToolGroup -->|/search| SearchHandler[Search Controller Handler]
    SearchHandler --> MW1[Auth Middleware]
    MW1 --> MW2[Rate Limit Middleware]
    MW2 --> Execution[Execute Search Tool]
```"""
    },
    "07_Serialization_and_Deserialization_for_backend_engineers": {
        "title": "7. Serialization and Deserialization for Backend Engineers",
        "diagram_1": """```mermaid
mindmap
  root((Serialization Systems))
    Formats
      JSON Human Readable / High CPU Overhead
      Protobuf Binary / Schema Strict / Ultra Fast
      MessagePack Compact Binary JSON
    Memory & Performance
      Zero-Copy Parsing
      CPU Framing & String Allocations
      Bandwidth Consumption on Wire
    AI Systems Impact
      MCP JSON-RPC Payload Serialization
      Vector Embedding Serialization Float32 Arrays
      FastAPI Pydantic Model Validation Latency
```""",
        "diagram_2": """```mermaid
graph LR
    Object[In-Memory Object / Python Dict] -->|Serialize| Bytes[Byte Stream / UTF-8 JSON / Protobuf]
    Bytes -->|Network Socket Transfer| Wire[Wire Transport]
    Wire -->|Receive Sockets| RecvBytes[Received Byte Stream]
    RecvBytes -->|Deserialize & Validate| TargetObj[Target In-Memory Data Structure]
```"""
    },
    "08_Authentication_and_authorization_for_backend_engineers": {
        "title": "8. Authentication and Authorization for Backend Engineers",
        "diagram_1": """```mermaid
mindmap
  root((Auth & AuthZ Architecture))
    Authentication Identity
      Stateful Sessions Redis Session Store
      Stateless JWT Cryptographic Signature HS256/RS256
      Password Hashing Argon2id / bcrypt
    Authorization Access
      RBAC Role-Based Access Control
      ABAC Attribute-Based Access Control
      Scopes & API Token Permissions
    Security Risks
      JWT Revocation Challenge
      Token Replay Attacks
      CSRF & XSS Mitigation
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    autonumber
    Client->>Server: POST /login (Credentials)
    Server->>DB: Fetch User & Hash
    Server->>Server: Verify Hash (Argon2id)
    Server->>Server: Generate JWT (Sign with Private Key RS256)
    Server-->>Client: 200 OK (Bearer JWT + Refresh Cookie)
    Client->>Server: GET /api/v1/agent (Header: Bearer JWT)
    Server->>Server: Validate Signature & Claims (Public Key)
    Server-->>Client: Authorized Resource Access
```"""
    },
    "09_Validations_and_transformations_for_backend_engineers": {
        "title": "9. Validations and Transformations for Backend Engineers",
        "diagram_1": """```mermaid
mindmap
  root((Input Processing Engine))
    Validation Types
      Syntactic Validation Schema Format Types
      Semantic Validation Business Rule Checking
      Security Sanitization Injection Prevention
    Transformations
      Data Normalization Trim Lowercase Strip
      Type Coercion String -> Int / Date
      DTO Mapping Request -> Domain Model
    AI Systems Application
      Prompt Input Sanitization & Guardrails
      Tool Call Schema Validation Pydantic / JsonSchema
      Output Structuring Structured Extraction
```""",
        "diagram_2": """```mermaid
graph TD
    Raw[Raw Network Input Payload] --> Val1[Schema & Type Validation]
    Val1 -->|Fail| Err1[422 Unprocessable Entity]
    Val1 -->|Pass| Sanit[Security Sanitization]
    Sanit --> Trans[Data Transformation & DTO Assembly]
    Trans --> Domain[Validated Domain Object for Business Logic]
```"""
    },
    "10_What_are_controllers_services_repositories_middlewares_and_request_context": {
        "title": "10. Controllers, Services, Repositories, Middlewares and Request Context",
        "diagram_1": """```mermaid
mindmap
  root((Backend Layered Architecture))
    Middlewares
      Cross-Cutting Concerns Logging / Auth / Rate Limit
      Request Context Propagation Trace ID / User Claims
    Controller Layer
      HTTP Protocol Translation
      Request Parsing & Status Code Response
    Service Layer
      Pure Business Logic Execution
      Orchestration of Multiple Repos / Tools
    Repository Layer
      Data Storage Abstraction
      SQL / NoSQL Query Execution
```""",
        "diagram_2": """```mermaid
graph TD
    Req[HTTP Request] --> MW[Middleware Chain: Auth -> TraceID -> Logger]
    MW --> Ctrl[Controller: Parses Params & Routes]
    Ctrl --> Svc[Service Layer: Business Rules Execution]
    Svc --> Repo[Repository Layer: DB Abstraction]
    Repo --> DB[(Database)]
    Svc --> Ext[External AI Tool / MCP Client]
```"""
    },
    "11_Complete_REST_API_Design": {
        "title": "11. Complete REST API Design",
        "diagram_1": """```mermaid
mindmap
  root((REST Architectural Constraints))
    Core Principles
      Stateless Protocol Interactions
      Resource-Oriented URIs /v1/documents/{id}
      Uniform Interface & Standard Verbs
    Idempotency & Safety
      Safe Verbs GET HEAD OPTIONS
      Idempotent Verbs PUT DELETE GET
      Non-Idempotent Verbs POST
    API Operations
      Pagination Cursor-Based vs Offset
      Error Handling Standard Problem Details RFC 7807
      Versioning Path vs Header Versioning
```""",
        "diagram_2": """```mermaid
graph LR
    Client[Client / Agent API Consumer] -->|GET /v1/chats?cursor=xyz&limit=20| API Gateway
    API Gateway --> Controller[Chat Controller]
    Controller --> Service[Pagination Service]
    Service --> DB[(PostgreSQL Index Lookup)]
    DB -- Cursor Result Set --> Service
    Service -- JSON API Payload + Next Cursor --> Client
```"""
    },
    "12_Mastering_Databases_with_Postgres": {
        "title": "12. Mastering Databases with Postgres",
        "diagram_1": """```mermaid
mindmap
  root((PostgreSQL Internals))
    Storage & Concurrency
      MVCC Multi-Version Concurrency Control
      Tuple Storage & Auto-Vacuuming
      WAL Write-Ahead Logging for Durability
    Indexing Strategies
      B-Tree Default Range & Equality
      GIN Generalized Inverted Index JSONB / Text
      IVFFlat / HNSW Vector Indexing pgvector
    Transaction Isolation
      Read Committed Default
      Repeatable Read & Serializable
      Row & Table Locking Mechanisms
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    autonumber
    Client->>Postgres: BEGIN TRANSACTION (Isolation Level: Repeatable Read)
    Client->>Postgres: UPDATE embeddings SET vector = [...] WHERE id = 42
    Postgres->>WAL: Append Change Record to Write-Ahead Log
    Postgres->>BufferPool: Modify Page Tuple in Shared Memory
    Postgres-->>Client: UPDATE 1 (Uncommitted State Visible to TX)
    Client->>Postgres: COMMIT
    Postgres->>WAL: Flush WAL Buffer to Disk (Durability Guaranteed)
    Postgres-->>Client: COMMIT SUCCESS
```"""
    },
    "13_Caching_the_secret_behind_it_all": {
        "title": "13. Caching, the Secret Behind It All",
        "diagram_1": """```mermaid
mindmap
  root((Caching Architecture))
    Caching Strategies
      Cache-Aside Read Through
      Write-Through / Write-Behind
      In-Memory vs Distributed Redis
    Cache Invalidation
      TTL Time-To-Live Expiry
      LRU / LFU Eviction Policies
      Cache Stampede Mitigation Probabilistic Early Expiration
    AI Systems Use Cases
      LLM Semantic Caching Similarity Lookup
      RAG Document Embedding Caching
      User Session & Rate Limit Tracking
```""",
        "diagram_2": """```mermaid
graph TD
    Req[Incoming Agent Request] --> CacheCheck{Check Redis / Semantic Cache}
    CacheCheck -->|Cache Hit| ReturnCache[Return Cached Completion < 5ms]
    CacheCheck -->|Cache Miss| LLMCall[Call LLM API / Execute Pipeline]
    LLMCall --> SaveCache[Write Response to Redis with TTL]
    SaveCache --> ReturnLLM[Return LLM Result to User]
```"""
    },
    "14_Task_queues_and_background_jobs": {
        "title": "14. Task Queues and Background Jobs",
        "diagram_1": """```mermaid
mindmap
  root((Background Job Processing))
    Architecture Components
      Producer API Endpoint
      Message Broker Redis Streams / RabbitMQ
      Worker Pool Celery / Asynchronous Workers
    Guarantees & Patterns
      At-Least-Once Delivery
      Visibility Timeouts & Worker Heartbeats
      Dead Letter Queue DLQ for Unhandled Failures
    Idempotency
      Idempotency Key Verification
      Distributed Locks Redlock
```""",
        "diagram_2": """```mermaid
graph LR
    API[FastAPI Producer] -->|Enqueue Job + Task ID| Broker[(Redis Broker / Message Queue)]
    Broker -->|Fetch Message| Worker1[Worker Instance 1]
    Broker -->|Fetch Message| Worker2[Worker Instance 2]
    Worker1 -->|Process Heavy RAG Ingestion| DB[(PostgreSQL)]
    Worker1 -->|On Failure after 3 retries| DLQ[(Dead Letter Queue)]
```"""
    },
    "15_Full_text_search_using_Elasticsearch_for_blazingly_fast_search": {
        "title": "15. Full Text Search Using Elasticsearch",
        "diagram_1": """```mermaid
mindmap
  root((Elasticsearch Architecture))
    Search Engine Core
      Inverted Index Term -> Doc ID Mapping
      Analysis Pipeline Character Filters / Tokenizer / Token Filters
      TF-IDF & BM25 Relevance Scoring
    Cluster Architecture
      Shards Primary & Replica Shards
      Cluster Node Types Master / Data / Ingest
      Distributed Query Execution Scatter-Gather
    Hybrid Search in AI
      BM25 Keyword Search + Vector Dense Embedding Search
      Reciprocal Rank Fusion RRF Scoring
```""",
        "diagram_2": """```mermaid
graph TD
    Doc[Raw Text Document] --> CharFilter[Character Filter: HTML Strip]
    CharFilter --> Tokenizer[Standard Tokenizer: Word Split]
    Tokenizer --> TokenFilter[Token Filters: Lowercase & Stemming]
    TokenFilter --> InvIndex[(Inverted Index Dictionary)]
```"""
    },
    "16_Error_Handling_and_Building_Fault_Tolerant_Systems": {
        "title": "16. Error Handling and Building Fault Tolerant Systems",
        "diagram_1": """```mermaid
mindmap
  root((Fault Tolerance Architecture))
    Resilience Patterns
      Circuit Breaker Closed / Open / Half-Open
      Exponential Backoff with Jitter
      Rate Limiting & Bulkhead Isolation
    Error Handling Philosophy
      Expected Domain Errors vs Unexpected System Crashes
      Graceful Degradation Fallbacks
      Structured Error Diagnostics RFC 7807
```""",
        "diagram_2": """```mermaid
stateDiagram-v2
    [*] --> Closed
    Closed --> Open: Failures > Threshold (500 Error Spikes)
    Open --> HalfOpen: Timeout Duration Expired (30s)
    HalfOpen --> Closed: Probe Request Succeeds
    HalfOpen --> Open: Probe Request Fails
```"""
    },
    "17_Production-grade_Configuration_Management": {
        "title": "17. Production-Grade Configuration Management",
        "diagram_1": """```mermaid
mindmap
  root((Configuration Engine))
    12-Factor Config
      Environment Variable Injection
      Separation of Code & Configuration
      Secret Management Vault / AWS Secrets Manager
    Dynamic Config
      Feature Flags & Runtime Toggles
      Hot-Reloading without Process Restart
      Strict Schema Validation Pydantic BaseSettings
```""",
        "diagram_2": """```mermaid
graph TD
    Env[Environment Vars / K8s Secrets] --> App[FastAPI Application Startup]
    App --> Settings[Pydantic BaseSettings Parser]
    Settings -->|Validation Failure| Crash[Fail Fast & Abort Process]
    Settings -->|Validation Success| Singleton[Type-Safe App Config Singleton]
```"""
    },
    "18_Logging_Monitoring_and_Observability": {
        "title": "18. Logging, Monitoring and Observability",
        "diagram_1": """```mermaid
mindmap
  root((Observability Pillar))
    Structured Logging
      JSON Formatted Logs
      Trace ID & Context Propagation
      Log Aggregation Vector / ELK / Datadog
    Metrics & Telemetry
      RED Method Rate Errors Duration
      USE Method Utilization Saturation Errors
      Prometheus Scraping & Grafana Dashboards
    Distributed Tracing
      OpenTelemetry Traces & Spans
      LLM Pipeline Latency Breakdown
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    participant Agent as AI Agent
    participant Gateway as API Gateway
    participant Service as LLM Service
    Agent->>Gateway: POST /run (Header: X-Trace-ID: abc-123)
    Gateway->>Service: Call Model (Context Span ID: span-1)
    Service-->>Gateway: Return Span Output (Duration: 250ms)
    Gateway-->>Agent: Response + Trace Headers
```"""
    },
    "19_Graceful_Shutdown": {
        "title": "19. Graceful Shutdown",
        "diagram_1": """```mermaid
mindmap
  root((Graceful Shutdown Lifecycle))
    Signal Handling
      SIGTERM Termination Signal from OS/K8s
      SIGINT Interrupt Signal Ctrl+C
      SIGKILL Forceful Immediate Termination
    Draining Sequence
      Stop Accepting New Connections
      Finish Active In-Flight Requests
      Drain Worker Task Queues
      Close DB Pools & Redis Connections
```""",
        "diagram_2": """```mermaid
graph TD
    OS[OS / Kubernetes sends SIGTERM] --> SigHandler[Trap SIGTERM Signal]
    SigHandler --> Step1[Set Readiness Probe to Unhealthy]
    Step1 --> Step2[Stop Accepting New Socket Connections]
    Step2 --> Step3[Wait for In-Flight HTTP Requests to Finish]
    Step3 --> Step4[Flush In-Memory Logs & Async Worker Buffers]
    Step4 --> Step5[Close DB Connection Pools & Redis Sockets]
    Step5 --> Exit[Exit Process with Code 0]
```"""
    },
    "20_Backend_Security_Everything_You_Need_to_Know": {
        "title": "20. Backend Security: Everything You Need to Know",
        "diagram_1": """```mermaid
mindmap
  root((Backend Security Infrastructure))
    Network & Transport Security
      TLS 1.3 Encryption in Transit
      CORS Cross-Origin Resource Sharing
      Rate Limiting DDoS Mitigation
    Application Security
      SQL Injection Prevention Parameterized Queries
      XSS & CSRF Protection Cookie Flags SameSite
      Input Sanitization & Output Encoding
    AI Security
      Prompt Injection Guardrails
      Data Leakage Prevention DLP
      Secure API Key Storage
```""",
        "diagram_2": """```mermaid
graph TD
    Attacker[Malicious Payload / SQLi / XSS] --> WAF[Web Application Firewall / Rate Limiter]
    WAF --> Sanitizer[Input Validation & Parameterized Binder]
    Sanitizer --> DB[(PostgreSQL Prepared Statements)]
    DB --> OutputEnc[Output Encoder]
    OutputEnc --> Client[Safe Client Response]
```"""
    },
    "21_Backend_Scaling_and_Performance_Engineering": {
        "title": "21. Backend Scaling and Performance Engineering",
        "diagram_1": """```mermaid
mindmap
  root((Scaling Engineering))
    Stateless Horizontal Scaling
      Load Balancing Nginx / HAProxy / AWS ALB
      Session Externalization to Redis
      Database Connection Pooling PgBouncer
    Database Scaling
      Read Replicas & Read/Write Splitting
      Sharding Horizontal Partitioning
      Indexing & Query Optimization
    Performance Tuning
      CPU vs I/O Bottlenecks
      Async I/O Event Loops asyncio /uvicorn
```""",
        "diagram_2": """```mermaid
graph TD
    UserReq[High Volume Traffic] --> ALB[Application Load Balancer]
    ALB --> Web1[FastAPI Server 1]
    ALB --> Web2[FastAPI Server 2]
    ALB --> Web3[FastAPI Server 3]
    Web1 -->|Writes| PrimaryDB[(Postgres Primary DB)]
    Web1 -->|Reads| Replica1[(Postgres Read Replica 1)]
    Web2 -->|Reads| Replica2[(Postgres Read Replica 2)]
    Web3 -->|Cache Lookups| RedisCluster[(Redis Cluster)]
```"""
    },
    "22_Concurrency_Parallelism_IO_Bound_vs_CPU_Bound": {
        "title": "22. Concurrency & Parallelism: IO Bound vs CPU Bound",
        "diagram_1": """```mermaid
mindmap
  root((Concurrency Architecture))
    IO-Bound Workloads
      Network Requests & DB Queries
      Event-Loop Non-Blocking Async/Await
      Cooperative Multitasking asyncio
    CPU-Bound Workloads
      Data Crunching & Vector Math
      Multiprocessing Parallel Execution
      GIL Global Interpreter Lock Impact
    AI Engineering Applications
      Parallel MCP Tool Execution asyncio.gather
      Background Vector Embedding Computation ProcessPool
```""",
        "diagram_2": """```mermaid
graph TD
    Task[Incoming Workload] --> CheckType{Workload Type?}
    CheckType -->|I/O Bound: API Calls / DB Queries| AsyncLoop[Asyncio Event Loop / Non-Blocking Single Thread]
    CheckType -->|CPU Bound: Embedding Math / Parsing| MultiProc[Multiprocessing Pool / Multiple CPU Cores]
    AsyncLoop --> ConcurrentRes[High Concurrent Throughput]
    MultiProc --> ParallelRes[True Parallel Execution]
```"""
    },
    "23_Object_Storage_Everything_You_Need_to_Know": {
        "title": "23. Object Storage - Everything You Need to Know",
        "diagram_1": """```mermaid
mindmap
  root((Object Storage Systems))
    Architecture
      Flat Namespace Bucket & Key
      Immutability Write Once Read Many WORM
      Distributed Replication High Availability
    Access Patterns
      Presigned URLs Direct Client Upload
      Multipart Upload for Large Files
      CDN Integration Edge Caching CloudFront
    AI Systems Integration
      Storing Audio / Video Transcripts
      Persisting Large Vector Index Snapshots
      Fine-Tuning Dataset Blob Storage
```""",
        "diagram_2": """```mermaid
sequenceDiagram
    autonumber
    Client->>FastAPI: POST /v1/upload-request (Filename, FileType)
    FastAPI->>FastAPI: Authorize & Generate Presigned S3 URL (TTL: 15m)
    FastAPI-->>Client: Return Presigned URL
    Client->>S3/ObjectStorage: PUT Binary File Payload (Direct to S3)
    S3/ObjectStorage-->>Client: 200 OK (Upload Complete)
    Client->>FastAPI: POST /v1/upload-confirm (FileKey)
```"""
    }
}

def format_into_paragraphs(text, target_words_per_para=120):
    words = text.split()
    if not words:
        return ""
    paragraphs = []
    for i in range(0, len(words), target_words_per_para):
        chunk = words[i:i + target_words_per_para]
        paragraphs.append(" ".join(chunk))
    return "\n\n".join(paragraphs)

def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "r", encoding="utf-8") as mf:
        manifest = json.load(mf)

    total_lessons = len(manifest)
    print(f"Starting master study notes generation for {total_lessons} lessons...\n")

    for idx, item in enumerate(manifest, 1):
        lesson_key = item["lesson"]
        meta = LESSON_METADATA.get(lesson_key, {
            "title": f"{idx}. {item['title']}",
            "diagram_1": "",
            "diagram_2": ""
        })

        # Check if subagent summaries exist first
        summary_files = sorted(glob.glob(os.path.join(WORK_DIR, lesson_key, "summary_*.md")))
        raw_chunks = []

        if summary_files:
            for sf in summary_files:
                with open(sf, "r", encoding="utf-8") as f:
                    raw_chunks.append(f.read().strip())
        else:
            chunk_files = sorted(glob.glob(os.path.join(WORK_DIR, lesson_key, "part_*.md")))
            for cf in chunk_files:
                with open(cf, "r", encoding="utf-8") as f:
                    raw_chunks.append(f.read().strip())

        full_raw_transcript = "\n\n".join(raw_chunks)
        word_count = len(full_raw_transcript.split())
        formatted_body = format_into_paragraphs(full_raw_transcript)

        # Build Master Study Note File
        doc = f"# {meta['title']}\n\n"
        doc += f"> [!IMPORTANT]\n"
        doc += f"> **AI Systems Engineering Master Study Notes** | **Total Words:** {word_count:,} | **Domain Target:** Arun Yadav (neural-arun)\n\n"
        doc += "## Architectural Mindmap & System Connectivity\n\n"
        if meta["diagram_1"]:
            doc += meta["diagram_1"] + "\n\n"

        doc += "## Core Engineering Workflow & Component Sequence\n\n"
        if meta["diagram_2"]:
            doc += meta["diagram_2"] + "\n\n"

        doc += "## Comprehensive Technical Lecture Breakdown\n\n"
        doc += formatted_body + "\n\n"

        doc += "---\n\n"
        doc += "### Key AI Systems Engineering Mappings\n"
        doc += "- **Production Architecture**: Direct mapping of lecture primitives to scalable microservices, FastAPI gateways, and PostgreSQL data stores.\n"
        doc += "- **Reliability & Resilience**: Circuit breakers, rate limits, and structured error handling applied to Agentic LLM tool calls and RAG pipelines.\n"
        doc += "- **Performance Optimization**: Zero-copy deserialization, connection pooling, and asynchronous event loops for maximum system throughput.\n"

        target_file = os.path.join(DEST_DIR, f"{lesson_key}_notes.md")
        with open(target_file, "w", encoding="utf-8") as out:
            out.write(doc)

        print(f"[{idx}/{total_lessons}] Generated: {os.path.basename(target_file)} ({word_count:,} words)")

    print(f"\nAll {total_lessons} master notes generated successfully in '{DEST_DIR}'.")

if __name__ == "__main__":
    main()
