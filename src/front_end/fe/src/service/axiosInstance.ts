import axios from "axios";
const baseURL = 'http://127.0.0.1:8000/';

let axiosInstance = axios.create({
    baseURL: baseURL,
    timeout: 500,
    headers: {
        'Authorization': 'Bearer',
		'Content-Type': 'application/json',
		'accept': 'application/json',
    }
});



export default axiosInstance;