import axios from "axios";
import API from "../api/api";

const login = async (username, password) => {
  try {
    const { data } = await axios.post(
      `${API}/auth/token`,
      { username, password },
      {
        headers: { "Content-Type": "application/json" },
      },
    );
    localStorage.clear();
    localStorage.setItem("token", data.access);
    localStorage.setItem("refresh_token", data.refresh);
    window.location.href = "/";
    return data;
  } catch (error) {
    console.error("Login failed:", error.response?.data || error.message);
    return null;
  }
};
const registerCustomer = async (username, email, password1, password2, firstName, lastName) => {
  try{
    const {data} = await axios.post(`${API}/customers/register`,{
    username, email, password1, password2, firstName, lastName
    },
    {
        headers: { "Content-Type": "application/json" },
      }
    );
    console.log("Registration successful", data);
    window.location.href = "/login";
    return data;
  }catch(error){
    console.error(
      "Registration failed:",
      error.response?.data || error.message
    );
    return null;
  }
}
const logout = async () => {
  try {
    const accessToken = localStorage.getItem('access_token');
    const response= await axios.post(
      "http://127.0.0.1:8000/api/logout/",
      { refresh_token: localStorage.getItem("refresh_token") },
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
        withCredentials: true,
      }
    );
    
    console.log("Logout successful", response);

    
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    window.location.href = "/login";
  } catch (error) {
    console.error("Logout failed:", error.response?.data || error.message);
    return null;
  }
};
export { login, logout, registerCustomer };