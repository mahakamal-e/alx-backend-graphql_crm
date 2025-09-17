from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import datetime

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    log_message = f"{timestamp} CRM is alive\n"

    # Append to log file
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(log_message)

        # Optional: check GraphQL hello field
        transport = RequestsHTTPTransport(
            url="http://localhost:8000/graphql",
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        query = gql("{ hello }")
        try:
            result = client.execute(query)
            f.write(f"{timestamp} GraphQL endpoint response: {result}\n")
        except Exception as e:
            f.write(f"{timestamp} GraphQL endpoint error: {e}\n")
