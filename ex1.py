import requests

def fetch_todos():
    """Fetches the todo list from JSONPlaceholder API and prints the first 10 items."""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()  # Convert the response to JSON format
        for todo in todos[:10]:  # Get the first 10 todos
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")

# Run the function
fetch_todos()
