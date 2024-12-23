
# Django CRUD API for Campaign Management

This is a simple Django-based REST API to manage campaigns, agents, and campaign results. The project allows you to perform CRUD operations (Create, Read, Update, Delete) on the following models:

- **Agent**: Represents an agent with a name, language, and voice ID.
- **Campaign**: Represents a marketing campaign, including campaign type, status, and the associated agent.
- **Campaign Results**: Stores the results of campaigns, such as cost, outcome, and call duration.

The API is built using Django and Django REST Framework (DRF) and supports interactions via HTTP methods (GET, POST, PUT, DELETE).

---

## Features

- Create, Read, Update, Delete Agents
- Create, Read, Update, Delete Campaigns
- Create, Read, Update, Delete Campaign Results
- Data is serialized to JSON format for easy integration with frontend or other applications.

---

## Requirements

- Python 3.10 or above
- Django 5.1.3 or above
- Django REST Framework (DRF)
- SQLite (default, can be switched to other databases)

---

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bentekku/voizer.ai_back-end_django_crud.git
    cd voizer.ai_back-end_django_crud
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For MacOS/Linux
    venv\Scripts ctivate     # For Windows
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the API**:
    Open your browser or API testing tool (e.g., Postman) and visit `http://127.0.0.1:8000/api/` to see the API in action.

---

## API Endpoints

### **Agent Endpoints**

- **GET /api/agents/**: List all agents
- **POST /api/agents/**: Create a new agent
- **GET /api/agents/{id}/**: Retrieve a specific agent by ID
- **PUT /api/agents/{id}/**: Update a specific agent by ID
- **DELETE /api/agents/{id}/**: Delete a specific agent by ID

### **Campaign Endpoints**

- **GET /api/campaigns/**: List all campaigns
- **POST /api/campaigns/**: Create a new campaign
- **GET /api/campaigns/{id}/**: Retrieve a specific campaign by ID
- **PUT /api/campaigns/{id}/**: Update a specific campaign by ID
- **DELETE /api/campaigns/{id}/**: Delete a specific campaign by ID

### **Campaign Results Endpoints**

- **GET /api/campaignresults/**: List all campaign results
- **POST /api/campaignresults/**: Create new campaign results
- **GET /api/campaignresults/{id}/**: Retrieve a specific campaign result by ID
- **PUT /api/campaignresults/{id}/**: Update a specific campaign result by ID
- **DELETE /api/campaignresults/{id}/**: Delete a specific campaign result by ID

---

## Models

### **Agent Model**

- `id`: Primary Key (Auto-generated)
- `agent_name`: Name of the agent (string)
- `language`: Language spoken by the agent (string)
- `voice_id`: Unique voice identifier (string)
- `updated`: DateTime of the last update (auto-generated)

### **Campaign Model**

- `id`: Primary Key (Auto-generated)
- `campaign_name`: Name of the campaign (string)
- `campaign_type`: Type of campaign (`Inbound`, `Outbound`)
- `phone_number`: Campaign's phone number (string)
- `status`: Campaign status (`Running`, `Paused`, `Completed`)
- `agent_name`: ForeignKey to `Agent` model (integer reference to agent)

### **CampaignResults Model**

- `id`: Primary Key (Auto-generated)
- `campaign_name`: Name of the campaign (string)
- `campaign_type`: Type of the campaign (string)
- `phone_number`: Phone number associated with the result (string)
- `cost`: Campaign cost (float)
- `outcome`: Outcome of the campaign (string)
- `call_duration`: Duration of the call (float)
- `recording`: URL of the campaign recording (string)
- `summary`: Summary of the campaign result (text)
- `transcription`: Transcription of the campaign result (text)

---

## Troubleshooting

### `db.sqlite3` Errors:
If you encounter any issues with the SQLite database, try deleting the `db.sqlite3` file and running migrations again:
```bash
rm db.sqlite3
python manage.py migrate
```

### CORS Issues:
If you're accessing the API from a frontend hosted on a different domain, you may need to configure CORS settings by installing and configuring `django-cors-headers`.

---
