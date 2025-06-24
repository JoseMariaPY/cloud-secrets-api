# 🔐 Parameter Store API - AWS Serverless

A Serverless API built with AWS Lambda and API Gateway to **create, read, update, delete, and list** secrets using **AWS Systems Manager Parameter Store**.

> ☁️ This is a hands-on project to practice AWS Serverless skills as a developer.

---
## 🚀 Tech Stack

- AWS Lambda (Python 3.13)
- AWS API Gateway
- AWS SSM Parameter Store
- Serverless Framework v4
- API Key Authentication
- Python + Boto3

---

## 📁 Project Structure

```
parameter-store-api/
├── serverless.yml
├── requirements.txt
└── src/
    ├── createParam.py
    ├── updateParam.py
    ├── getParam.py
    ├── deleteParam.py
    └── listParams.py
```

---

## 🔐 Authentication

All endpoints are protected using an **API Key**.

**Required Header:**

```
x-api-key: YOUR_API_KEY
```

---

## 📡 Available Endpoints

### API Documentation (OpenAPI / Swagger)
This project includes a full OpenAPI 3.0 specification (openapi.yaml) to describe all available endpoints.

You can explore and test the API visually using Swagger Editor:

🔗 Open in Swagger Editor

1. Click the link above

2. Paste or upload openapi.yaml

3. Interact with the API in the browser!

### ✅ Create Parameter

```http
POST /parameters
```

**Body:**

```json
{
  "name": "/myapp/github",
  "value": "super-secret",
  "type": "SecureString"
}
```

---

### 🔄 Update Parameter

```http
PATCH /parameters
```

**Body:**

```json
{
  "name": "/myapp/github",
  "value": "updated-value"
}
```

---

### 📥 Get Parameter

```http
GET /parameters
```

**Header:**

```
x-parameter-name: /myapp/github
```

---

### 🗑️ Delete Parameter

```http
DELETE /parameters
```

**Header:**

```
x-parameter-name: /myapp/github
```

---

### 📃 List Parameters by Path

```http
GET /parameters/list
```

**Header:**

```
x-parameter-path: /myapp/
```

---

## 🚀 Deploy

```bash
serverless deploy
```

---

## 🔑 Retrieve Your API Key

```bash
aws apigateway get-api-keys --name-query parameterApiKey --include-values
```

Or through the AWS Console > API Gateway > API Keys.

---

## 👨‍💻 Author

**José Duarte**  
[LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/your-username)

---

## 📜 License

MIT
