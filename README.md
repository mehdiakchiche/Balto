\# Django + Qt Application



\## Installation

```bash

python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate

pip install -r requirements.txt



\# Variables d’environnement



Dans Django (settings.py) :

SECRET\_KEY = os.getenv("SECRET\_KEY")







