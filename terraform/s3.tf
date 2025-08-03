resource "aws_s3_bucket" "input" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket" "output" {
  bucket = "${var.bucket_name}-output"
}
