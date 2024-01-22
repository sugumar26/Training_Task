provider "google" {
  project = "bustling-syntax-405306"
  region  = "us-central1"
  credentials = file("C:\\Users\\HI\\Downloads\bustling-syntax-405306-0abc624c5bd9.json")
}

terraform {
#   backend "local" {
#     path = "terraform.tfstate"
#   }

  backend "gcs" {
    bucket  = "sugumar-spark"
    prefix  = "statefile"
  }
}

variable "bucket_name" {
  type    = string
  default = "sample-bucket007"
}

resource "google_storage_bucket" "bucket007" {
  name          = var.bucket_name
  location      = "US"
  force_destroy = true
}

resource "random_id" "example" {
  byte_length = 8
}

resource "google_storage_bucket_object" "example" {
  name   = "example-${random_id.example.hex}"
  bucket = google_storage_bucket.bucket007.name
  source = "C:\\Users\\HI\\OneDrive\\Desktop\\terraform Hands On\\Source\\sample.txt"
  depends_on = [google_storage_bucket.bucket007]
}

output "bucket_url" {
  value = google_storage_bucket.bucket007.url
}

output "object_url" {
  value = google_storage_bucket_object.example.self_link
}
