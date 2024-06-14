## About Amazon Connect Contact Search Tool
This solution can be used to search contact with specified attributes in Amazon Connect.

### Installation

Clone the repo

```bash
git clone https://github.com/photosphere/lex-v2-chat.git
```

cd into the project root folder

```bash
cd lex-v2-chat
```

#### Create virtual environment

##### via python

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment.

On Linux, or OsX 

```bash
source .venv/bin/activate
```
On Windows

```bash
source.bat
```

Then you should install the local requirements

```bash
pip install -r requirements.txt
```
### Build and run the Application Locally

```bash
streamlit run lex-v2-chat.py
```

### Or Build and run the Application on Cloud9

```bash
streamlit run lex-v2-chat.py --server.port 8080 --server.address=0.0.0.0
```

### Configuration screenshot
<img width="1044" alt="Flow Parser" src="https://github.com/photosphere/lex-v2-chat/assets/3398595/22d9dbe3-7546-4ee9-8ca3-053270381eff">
