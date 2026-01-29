import axios from "axios"

const URL = "http://127.0.0.1:8000/api"

const API = axios.create({
  baseURL: URL,
})

API.interceptors.request.use(
  (res) => {
    const token = localStorage.getItem("token")
    if (token) {
      res.headers.Authorization = `Bearer ${token}`
    }
    return res
  }
)

export default API
