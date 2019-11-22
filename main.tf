provider "heroku" {
  version = "~> 1.5"
}
provider "cloudflare" {
  version = "~> 1.9"
}
terraform {
  backend "s3" {
    bucket  = "crowdbotics-terraform"
    key     = "dj20191122_01_dev_1116"
    region  = "us-east-1"
    encrypt = "true"
  }
}
