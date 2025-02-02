### Network Security Project For Phising Data

This project is designed to provide network security services using Docker containers deployed on AWS EC2 instances. The project utilizes AWS ECR for container image storage and AWS S3 for data storage.

## Project Structure
    
    .
    ├── .github/
    │   └── workflows/
    │       └── main.yml
    ├── app.py
    ├── data_schema/
    │   └── schema.yaml
    ├── dataset/
    │   └── phishingData.csv
    ├── Dockerfile
    ├── final_model/
    │   ├── model.pkl
    │   └── preprocessing.pkl
    ├── main.py
    ├── notebooks/
    │   └── __init__.py
    ├── prediction_output/
    │   ├── __init__.py
    │   └── output.csv
    ├── push_data.py
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    ├── src/
    │   ├── cloud/
    │   ├── components/
    │   ├── constant/
    │   ├── entity/
    │   ├── exception/
    │   ├── logging/
    │   ├── pipeline/
    │   └── utils/
    ├── static/
    │   └── __init__.py
    ├── templates/
    │   ├── __init__.py
    │   └── table.html
    ├── test_mongodb.py
    ├── valid_data/
    │   └── test.csv
    └── venv/
    


## Prerequisites

- Docker
- AWS CLI
- Python 3.8+
- pip

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up AWS credentials:**

    Configure your AWS CLI with the necessary credentials:

    ```sh
    aws configure
    ```

4. **Build and push Docker image to ECR:**

    ```sh
    docker build -t your-ecr-repo-name .
    docker tag your-ecr-repo-name:latest your-ecr-uri/your-ecr-repo-name:latest
    docker push your-ecr-uri/your-ecr-repo-name:latest
    ```

## Deployment

1. **Deploy on EC2:**

    Use the following command to run the Docker container on an EC2 instance:

    ```sh
    docker run -d -p 8080:8080 --ipc="host" --name=networksecurity -e 'AWS_ACCESS_KEY_ID=your-access-key-id' -e 'AWS_SECRET_ACCESS_KEY=your-secret-access-key' -e 'AWS_REGION=your-region' your-ecr-uri/your-ecr-repo-name:latest
    ```

2. **Continuous Integration and Deployment:**

    The project uses GitHub Actions for CI/CD. The workflow is defined in [main.yml](https://github.com/AnimeshBasak-14/NetworkSecurity/blob/main/.github/workflows/main.yml). It includes steps for linting, running unit tests, building and pushing Docker images to ECR, and deploying the container on EC2.

## Usage

- **Access the application:**

    Once the container is running, you can access the application at `http://<ec2-instance-public-ip>:8080`.

- **Data Storage:**

    The project uses AWS S3 for storing data. Ensure that your S3 bucket is properly configured and accessible.


