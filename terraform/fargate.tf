resource "aws_ecs_cluster" "this" {
  name = "serverless-fargate-cluster"
}

resource "aws_ecs_task_definition" "this" {
  family                   = "file-processor"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.fargate_task_exec_role.arn
  task_role_arn            = aws_iam_role.fargate_task_exec_role.arn

  container_definitions = jsonencode([
    {
      name      = "file-processor",
      image     = "your-dockerhub-username/file-processor:latest", # Update this
      essential = true,
      environment = [
        { name = "BUCKET", value = var.bucket_name },
        { name = "INPUT_KEY", value = "PLACEHOLDER" }
      ],
      logConfiguration = {
        logDriver = "awslogs",
        options = {
          awslogs-group         = "/ecs/file-processor",
          awslogs-region        = var.aws_region,
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

resource "aws_cloudwatch_log_group" "ecs_logs" {
  name              = "/ecs/file-processor"
  retention_in_days = 7
}
