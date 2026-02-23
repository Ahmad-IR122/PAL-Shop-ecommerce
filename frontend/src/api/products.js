import API from "./api";

export const getAllProducts = async () => {
  try {
    const response = await API.get("products/products-list/");
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};

export const getProductById = async (id) => {
  try {
    const response = await API.get(`/products/products-detail/${id}/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching product by ID:", error);
    throw error;
  } 
}

