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

