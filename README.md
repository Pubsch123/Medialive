# MediaLive Channel Management

This repository provides Python scripts to manage an AWS Elemental MediaLive channel. It includes functions to start and stop a MediaLive channel, as well as check its current status. The script uses the AWS SDK for Python (Boto3) to interact with the MediaLive service.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have an AWS account with necessary permissions to manage MediaLive channels.
- You have AWS credentials configured on your machine.
- You have Python 3.x installed on your machine.

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:
```sh
git clone <repository_url>
```
Replace `<repository_url>` with the actual URL of the repository.

### 2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

#### On Windows
```sh
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required Python packages:
```sh
pip install boto3
```

### 4. Configure AWS Credentials
Configure your AWS credentials. You can do this using the AWS CLI:
```sh
aws configure
```
Alternatively, set the following environment variables:
```sh
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
export AWS_DEFAULT_REGION=your_region
```

## Usage

### Description of Functions
- **is_medialive_channel_active**: Checks if the MediaLive channel is currently active.
- **start_medialive_channel**: Starts the MediaLive channel if it is not already running.
- **stop_medialive_channel**: Stops the MediaLive channel if it is currently running.

### Example Usage
The `main` function demonstrates how to use the provided functions to manage a MediaLive channel. You can uncomment the relevant lines to either start or stop the MediaLive channel.

#### To Start the MediaLive Channel
Uncomment the line `start_medialive_channel()` in the `main` function and comment out the `stop_medialive_channel()` line:
```python
def main():
    # Start or stop MediaLive channel. Check both the functions one by one.
    start_medialive_channel()
    # stop_medialive_channel()
```
Run the script:
```sh
python script.py
```

#### To Stop the MediaLive Channel
Keep the line `stop_medialive_channel()` uncommented in the `main` function:
```python
def main():
    # Start or stop MediaLive channel. Check both the functions one by one.
    # start_medialive_channel()
    stop_medialive_channel()
```
Run the script:
```sh
python script.py
```

## Error Handling
The script includes basic error handling to catch and print exceptions that may occur during AWS API calls. Ensure that your AWS credentials and permissions are correctly configured to avoid authorization errors.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!
