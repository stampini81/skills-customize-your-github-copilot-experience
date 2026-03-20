# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI application with endpoints that allow users to create and retrieve items. Focus on organizing routes clearly and returning consistent JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI app with at least three endpoints: `GET /`, `GET /items`, and `POST /items`.
- Return JSON responses for all endpoints.
- Store items in an in-memory list while the app is running.


### 🛠️ Add Validation and Error Handling

#### Description
Use Pydantic models to validate incoming data and handle common errors so API responses remain clear and predictable for clients.

#### Requirements
Completed program should:

- Define a Pydantic model for item creation with fields such as `name` and `price`.
- Reject invalid input (for example, missing name or negative price) with clear FastAPI validation errors.
- Return a `404` response with a helpful message when a requested item ID does not exist.
