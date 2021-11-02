## **w3p: A Web3 + Python + Django Example**

---

### **Table of Contents**
  - [**Prerequisites**](#prerequisites)

---

### **Prerequisites**
#### **Infura**
You must [sign up for an account at Infura](https://infura.io/register) in order for the ethSrv to work properly.

After signing up, click on the [Ethereum tab](https://infura.io/dashboard/ethereum) and then "Create New Project". Enter a name and when at the "Project Settings" page, take a look at your ``PROJECT ID`` and ``PROJECT SECRET``.

Take a note of these and set them in your environment tables:
```bash
# Replace PROJECT ID with your Infura Project ID
# Replace PROJECT SECRET with your Infura Project Secret
export WEB3_INFURA_PROJECT_ID=PROJECT ID
export WEB3_INFURA_API_SECRET=PROJECT SECRET
```
You'll need to run that every time you start a new terminal, a workaround is setting the same commands to run in your ``~/.bashrc`` when starting up a new terminal:
```bash
# Open your ~/.bashrc file with the Nano editor
nano ~/.bashrc

# At the very end of the file, add these two lines
# Replace PROJECT ID with your Infura Project ID
# Replace PROJECT SECRET with your Infura Project Secret
export WEB3_INFURA_PROJECT_ID=PROJECT ID
export WEB3_INFURA_API_SECRET=PROJECT SECRET
```

#### **MariaDB / MySQL**
**Ubuntu/Debian:** ``sudo apt update && sudo apt install mariadb-server``\
**Arch Linux:** ``sudo pacman -Sy mariadb``

**Setup**
```bash
# Install the MariaDB system tables
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

# Enable/Start the MariaDB service
sudo systemctl enable mariadb && sudo systemctl start mariadb

# Secure the MariaDB installation
# Select default prompts with enter and create a password for the MariaDB root user when prompted.
sudo mysql_secure_installation

# Login to the MariaDB SQL shell
# Enter the root password you just created when prompted.
mariadb -u root -p
```
```sql
-- Create a new user for w3pDjango
-- Replace YOURPASSWORD with a secure password.
CREATE USER 'w3pDjango'@'localhost' IDENTIFIED BY 'YOURPASSWORD';

-- Create a new database for w3pDjango
CREATE DATABASE w3pDjango;

-- Grant all privileges on the database to the new user
GRANT ALL PRIVILEGES ON w3pDjango.* TO `w3pDjango`@`localhost`;

-- Flush privileges
FLUSH PRIVILGES;

--Exit the MariaDB SQL shell
exit;
```
In `w3pDjango/w3pDjango/settings.py` find ``DATABASES = {`` and change ``'PASSWORD': 'YOURPASSWORD',`` to the password you created for the w3pDjango user above.


#### **Pip**
You'll need the ``web3``, ``django`` and ``mysqlclient`` pip packages:

```bash
pip install web3 django mysqlclient
```

---