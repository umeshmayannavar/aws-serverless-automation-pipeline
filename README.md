# 🛠️ Serverless File Processing Pipeline (Fargate + Lambda + S3)

This repo sets up a **serverless automation pipeline** to process files uploaded to S3 using **AWS Lambda** to trigger **ECS Fargate tasks**.

---

## 🔧 Stack Used

- AWS S3
- AWS Lambda (Trigger)
- ECS Fargate (File Processor)
- CloudWatch Logs
- Terraform + Python

---

## ⚙️ How It Works

1. User uploads a file to `input/` folder in S3
2. Lambda is triggered
3. Lambda runs an ECS Fargate task
4. Fargate container reads the file → processes it (uppercase) → writes result to `output/`

---

## 🚀 Deploy Steps

### 1. Terraform Setup

```bash
cd terraform
terraform init
terraform apply
