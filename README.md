Base64 and Base32 Decoder

This Python script decodes data encoded in base64 and base32 formats. It accepts input in the form of command-line arguments and provides the decoded output.

Table of Contents

1. Usage
2. Installation
3. Examples
4. Version
5. License

---

1. Usage

To use this script, you need to provide the data you want to decode using the --b64 or --b32 flags.

- To decode data in base64 format, use the --b64 flag followed by the base64-encoded data you want to decode. You can provide one or more base64 strings for decoding.

  Example:

python script.py --b64 aGVsbG8= d29ybGQ=

- To decode data in base32 format, use the --b32 flag followed by the base32-encoded data you want to decode. You can provide one or more base32 strings for decoding.

Example:

python script.py --b32 JBSWY3DPEB3W64TMMQQQ====


2. Installation

To use this script, you can clone the repository from GitHub. Here are the steps:

- Open your terminal.
- Navigate to the directory where you want to clone the repository.
- Run the following command:

git clone https://github.com/nipunnegi2/new_64decoder.git

- After cloning, navigate to the repository directory:

cd yourrepository

Now you can use the script as described in the "Usage" section.

---

3. Examples

Here are some example commands for using the script:

- Decode Base64

Example:

python script.py --b64 aGVsbG8= d29ybGQ=



This will decode the base64-encoded strings and display the decoded text.

- Decode Base32

Example:

python script.py --b32 JBSWY3DPEB3W64TMMQQQ==== ME=======


This will decode the base32-encoded strings and display the decoded text.

---

4. Version

This script is version 1.0.

---

5. License

This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to use and modify this script as needed. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

Happy decoding!
