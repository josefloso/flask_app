# IP Reverser Web Application
This project demonstrates how to create a simple web application in Python that reverses the origin public IP of any request it receives. It also includes a bonus feature to store the reversed IP in a database.

### Prerequisites
`Python 3.x` 
`Docker` - installed to build and run the application in a container.
Basic knowledge of `Flask`, a lightweight web framework for Python.
Access to a `Kubernetes cluster on AWS` for deployment.

### Getting Started

Step 1: Clone the Repository
Clone this repository to your local machine:

git clone https://github.com/yourusername/ip-reverser.git
cd ip-reverser

Step 2: Install Dependencies
Ensure you have Python and pip installed, then install the necessary dependencies:

`pip install flask`

Step 3: Run the Application Locally
Run the Flask application locally to test it:

`export FLASK_APP=app.py`
`flask run`

Access the application in a web browser at http://localhost:8080.

Step 4: Containerize the Application with Docker
Build a Docker image of the application:

`docker build -t ip-reverser .`
Run the Docker container:

`docker run -p  8080:8080 ip-reverser`

Step 5: Create a Helm Chart
Initialize a new Helm chart:

`helm create ip-reverser-chart`
Modify the values.yaml and templates under the ip-reverser-chart/templates.

Step 6: Set Up GitHub Actions
Create a GitHub Actions workflow file .github/workflows/ci-cd.yml to automate the build, push, and deployment of the Docker image to a registry and then to your Kubernetes cluster.

Step 7: Deploy to AWS
Ensure you have configured your AWS credentials properly on your local machine and that you have access to your EKS cluster. You can use the AWS CLI to manage your Kubernetes resources.
