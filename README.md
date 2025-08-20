# 🔐 Password Manager

A simple **Password Manager** built with Python and Tkinter.  
This application allows users to **generate secure random passwords**, save them along with the website and username/email, and copy them to the clipboard for quick use.  

---

## ✨ Features

- **Password Generator**  
  - Creates strong, random passwords with a mix of letters, numbers, and symbols.
  - Passwords are automatically copied to your clipboard for convenience.

- **Save Credentials**  
  - Stores website, email/username, and password in a local `data.txt` file.
  - Ensures no empty fields before saving.
  - Confirms details with the user before writing to file.

- **Simple UI**  
  - Built with **Tkinter** for a clean and functional interface.
  - Includes input fields for website, email/username, and password.
  - One-click password generation and save functionality.

---

## 🛠️ Technologies Used

- [Python 3](https://www.python.org/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – for the graphical user interface  
- [Pyperclip](https://pypi.org/project/pyperclip/) – for copying passwords to clipboard  

---

## 📂 Project Structure

```
.
├── logo.png          # App logo displayed in the UI
├── data.txt          # Saved credentials (created automatically)
├── main.py           # Main application file (your script)
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SasaCejic/password-manager.git
cd password-manager
```

### 2. Install Dependencies
Make sure you have Python 3 installed. Then install required packages:
```bash
pip install pyperclip
```

### 3. Run the Application
```bash
python main.py
```

---

## 📖 Usage

1. Enter the **Website** and **Email/Username**.  
2. Click **Generate Password** to create a random secure password.  
   - The password will also be copied to your clipboard.  
3. Click **Add** to save the credentials to `data.txt`.  
4. Credentials are stored in the following format:
   ```
   Website  |   Email/Username  |   Password
   ```

---

## ⚠️ Disclaimer

This project is for **educational purposes** only.  
The data is saved in plain text (`data.txt`), which is **not secure for real-world use**.  
If you want to use this in production, consider:
- Encrypting stored credentials
- Using a secure database or password vault
- Adding authentication before accessing saved data

---

## 📸 Screenshot

<p align="center">
  <img src="screenshot.png" alt="Password Manager Logo" width="150"/>
</p>

---

## 📌 Future Improvements

- Implement search functionality for saved credentials.  
- Encrypt stored passwords.  
- Improve UI/UX with themes.  
- Add delete/edit functionality for saved records.

---

## 👨‍💻 Author

Developed by **Saša Ćejić**  
📧 Contact: cejicsasa17@gmail.com  

---

## 📝 License

This project is licensed under the MIT License.  
Feel free to use and modify for personal or educational purposes.


