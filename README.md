# Cloud9 Scout - API

> **Related Repositories:**
> - 🖥️ Frontend UI: [c9-scout-ui](https://github.com/AvishKaushik/c9-scout-ui)

FastAPI backend for generating AI-powered scouting reports for League of Legends and VALORANT esports teams.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- GRID API key ([Get access](https://grid.gg/get-access/))
- Groq API key ([Get free key](https://console.groq.com/))

### Installation

```bash
# Clone the repository
cd c9-scout-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r category2-opponent-scout/requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running the Server

```bash
cd category2-opponent-scout
uvicorn app.main:app --reload --port 8001
```

The API will be available at `http://localhost:8001`

---

## ⚙️ Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GRID_API_KEY` | Your GRID API key for match data | ✅ |
| `GROQ_API_KEY` | Groq API key for LLM features | ✅ |
| `USE_MOCK_DATA` | Set to `true` for development without API | ❌ |
| `CORS_ORIGINS` | Allowed origins (default: `*`) | ❌ |

---

## 📡 API Endpoints

### Team Search

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/scout/teams?query={name}` | Search for teams by name |

### Scouting Reports

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/scout/report` | Generate comprehensive scouting report |

**Request Body:**
```json
{
  "team_id": "12345",
  "game": "Valorant",
  "match_count": 10
}
```

**Response includes:**
- Executive summary
- Team composition preferences
- Player threat profiles
- Win/loss patterns
- Preparation priorities

### Counter Strategy

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/scout/counter` | Get AI-generated counter-strategies |

### Threat Analysis

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/scout/threats` | Rank enemy players by threat level |

### Map Statistics (VALORANT)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/scout/maps/{team_id}` | Get attack/defense stats per map |

### Report History

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/scout/history` | Get previously generated reports |

---

## 🏗️ Project Structure

```
c9-scout-api/
├── .env                          # Environment variables
├── category2-opponent-scout/
│   ├── app/
│   │   ├── main.py               # FastAPI application entry
│   │   ├── routers/
│   │   │   ├── scout.py          # Scouting report endpoints
│   │   │   ├── threats.py        # Threat ranking endpoints
│   │   │   └── counter.py        # Counter-strategy endpoints
│   │   ├── services/
│   │   │   ├── opponent_analyzer.py   # Team pattern analysis
│   │   │   ├── player_profiler.py     # Individual player profiling
│   │   │   ├── composition_tracker.py # Meta and comp tracking
│   │   │   └── counter_generator.py   # Counter-strategy generation
│   │   └── models/
│   │       └── schemas.py        # Pydantic models
│   └── requirements.txt
└── shared/                       # Shared utilities
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Framework | FastAPI |
| Language | Python 3.10+ |
| LLM | Groq (llama-3.3-70b-versatile) |
| Data Source | GRID GraphQL API |
| Validation | Pydantic v2 |
| Server | Uvicorn |

---

## 📚 API Documentation

Once running, access the interactive API docs:
- **Swagger UI**: https://c9-scout-api.onrender.com/docs
