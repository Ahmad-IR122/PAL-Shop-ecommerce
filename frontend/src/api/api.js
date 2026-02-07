import axios from "axios"

const URL = "http://127.0.0.1:8000/api"

const API = axios.create({
  baseURL: URL,
})

export default API
