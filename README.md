# 🚀 AWS EC2 Metadata Query Script

Welcome! This is a simple, secure Python script that helps you fetch the metadata of an AWS EC2 instance. This tool will help retrieve all the AWS EC2 metadata keys or just a specific key (like instance ID) in a JSON format.

## 🌟 What Does It Do?

- **Securely fetches AWS EC2 metadata** using AWS’s latest IMDSv2 protocol.
- **Prints the results in JSON**
- **Lets you ask for a specific key** (like `instance-id`) or you can retrieve all at once.
- **Lightweight**—just Python and the `requests` library.

## 🛠 Requirements

- Python 3.9
- [pipenv](https://pipenv.pypa.io/en/latest/) (recommended, but you can use pip too)
- An AWS EC2 instance (this script only works from inside EC2!)

## 🚦 Getting Started

1. **Clone this repo:**
   ```
   git clone https://github.com/swarajraja/aws-ec2-metadata-query.git
   cd aws-ec2-metadata-query
   ```

2. **Install dependencies with pipenv:**
   ```
   pipenv install
   ```

## 🏃 Usage

- **See all available metadata:**
  ```
  pipenv run python get_metadata_key.py
  ```

- **Look for a specific metadata key (e.g., your instance ID):**
  ```
  pipenv run python get_metadata_key.py instance-id
  ```

## 🛠️ How It Works

1. **Connects to the EC2 Metadata Service**  
   The script connects to the AWS metadata service available at `http://169.254.169.254`—but only from inside an EC2 instance.

2. **Uses IMDSv2 for Security**  
   Before getting any metadata, the script first requests a temporary session token (IMDSv2). This token is required for all subsequent metadata requests, making things more secure.

3. **Fetches Metadata**  
   - **All Metadata:** If you don’t specify a key, the script retrieves a list of all metadata keys, then fetches the value for each one.
   - **Specific Key:** If you provide a key (like `instance-id`), it fetches just that value.

4. **Outputs result in JSON format**  
   The results are printed in a formatted JSON.


