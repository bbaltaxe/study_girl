resource "aws_s3_bucket" "b" {
  bucket = "study-girl"
  acl    = "private"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
