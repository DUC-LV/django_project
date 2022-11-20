import { METHODS } from "http";
import axiosInstance from "./axiosInstance";

const getHome = {
    getAll(){
        const url = '/book'
        return axiosInstance.get(url)
    }
}
export default getHome;