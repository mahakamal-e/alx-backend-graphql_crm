import datetime
import requests

def log_crm_heartbeat():
    """
    Logs a heartbeat message every 5 minutes to /tmp/crm_heartbeat_log.txt.
    Optionally checks the GraphQL endpoint.
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    # Append to log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)

    # Optional: query GraphQL hello field to verify endpoint
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.status_code == 200:
            f.write(f"{timestamp} GraphQL endpoint is responsive\n")
        else:
            f.write(f"{timestamp} GraphQL endpoint returned status {response.status_code}\n")
    except Exception as e:
        f.write(f"{timestamp} GraphQL endpoint error: {e}\n")
