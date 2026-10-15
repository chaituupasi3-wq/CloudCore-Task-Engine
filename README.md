<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<div class="container">
    <span class="badge">Production-Style DevOps Project</span>
    <h1>DevOps TaskFlow Platform</h1>
    <p>A production-style, containerized task management API platform built to demonstrate end-to-end DevOps engineering, Infrastructure as Code (IaC), and automated CI/CD pipelines[cite: 1].</p>

  <h2>🏗️ Architecture Overview</h2>
    <pre><code>User 
    
    
  </code></pre>
    <ul>
        <li><strong>Infrastructure Provisioning:</strong> Terraform (VPC, Subnets, EC2, RDS, IAM, S3)[cite: 1]</li>
        <li><strong>Containerization:</strong> Docker & Docker Compose[cite: 1]</li>
        <li><strong>CI/CD Automation:</strong> GitHub Actions (Lint, Test, Build, Push to ECR) & Jenkins (Automated deployment)[cite: 1]</li>
        <li><strong>Serverless Operations:</strong> AWS Lambda & EventBridge (Scheduled automated database cleanups)[cite: 1]</li>
    </ul>

  <h2>🚀 Key Features</h2>
    <ul>
        <li><span class="highlight">RESTful API Architecture:</span> Full CRUD task operations supporting dynamic endpoint integration.</li>
        <li><span class="highlight">Database Persistence:</span> Backed by PostgreSQL with robust volume mounting.</li>
        <li><span class="highlight">Nginx Reverse Proxy:</span> Seamless path forwarding handling frontend assets and proxying backend communication.</li>
        <li><span class="highlight">Cloud-Ready Automation:</span> Built from scratch with scalability and portfolio deployment standards in mind[cite: 1].</li>
    </ul>

  <h2>🛠️ Tech Stack</h2>
    <p><strong>Languages & Frameworks:</strong> Python, Flask, JavaScript, HTML/CSS<br>
    <strong>Cloud & DevOps:</strong> AWS (EC2, RDS, S3, IAM), Terraform, Docker, Nginx<br>
    <strong>Automation & CI/CD:</strong> GitHub Actions, Jenkins, Bash Scripting[cite: 1]</p>

  <h2>🏃‍♂️ Quick Start (Local Development)</h2>
    <p>To run the entire platform locally using Docker Compose:</p>
    <pre><code># 1. Clone your repository
git clone https://github.com/your-username/devops-taskflow.git
cd devops-taskflow

# 2. Build and start containers
docker compose up --build</code></pre>

  <h3>Access Endpoints:</h3>
    <ul>
        <li><strong>Frontend UI:</strong> <code class="highlight">http://localhost:8080</code>[cite: 5]</li>
        <li><strong>Backend API Health Check:</strong> <code class="highlight">http://localhost:8000</code>[cite: 5]</li>
    </ul>

  <h2>📁 Directory Structure</h2>
    <pre><code>devops-taskflow/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── nginx.conf
├── k8s/
│   └── (Kubernetes deployment & service manifests)
├── compose.yaml
└── README.html</code></pre>
</div>

</body>
</html>
