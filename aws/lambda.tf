provider "aws" {
  region = "us-west-2"
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "study_girl_lambda" {
  filename         = "../study_chat.zip"
  function_name    = "study_chat"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "main.lambda_handler"
  source_code_hash = "${base64sha256(file("../study_chat.zip"))}"
  runtime          = "python3.6"
  
}
