from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def welcome():
	return "Welcome to Synthetic CAN Data CSV Generator ********** To Generate the CSV file, inside the server goto: http://172.21.1.110:5000/generate_csv ********** After you recieve the message: CSV file generated successfully, goto: http://172.21.1.110:5000/download_csv, to downlad the resulting data.csv file"

@app.route('/generate_csv', methods=['GET'])
def generate_csv():
    # Run your commands to generate the data.csv file
	os.system("apt update")
	os.system("apt upgrade -y")
	os.system("apt update")
	os.system("apt install can-utils")
	os.system("modprobe can")
	os.system("modprobe vcan")
	os.system("ip link add dev vcan0 type vcan")
	os.system("ip link set up vcan0")
	os.system("timeout 10s cangen vcan0 -g 200 &")
	os.system("timeout 5s candump vcan0 -t d -i | sed -e 's/(//g' -e 's/)  vcan0  /,/g' -e 's/   //g' -e 's/\[/,/g' -e 's/\]/,/g' -e 's/  //g' -e 's/ /,/2g' >> data.csv")

	return "CSV file generated successfully. You can download it from: http://172.21.1.110:5000/download_csv"

@app.route('/download_csv', methods=['GET'])
def download_csv():
    try:
        return send_file('data.csv', as_attachment=True)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)