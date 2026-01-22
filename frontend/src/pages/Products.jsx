import React, { useEffect, useState } from "react";
import { getAllProducts } from "../api/products";

const Products = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchProducts = async () => {
    try {
      const data = await getAllProducts();
      setProducts(data);
      console.log("Fetched products:", data);
    } catch (error) {
      console.error("Error fetching products:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Products</h2>
      {products.length > 0 ? (
        products.map((p) => {
          return (
            <div key={p.id}>
              <img
                src={p.image}
                alt={p.name}
                style={{ width: "150px", height: "auto" }}
              />
              {p.name} - ${p.price}
            </div>
          );
        })
      ) : (
        <div>No products available.</div>
      )}
    </div>
  );
};

export default Products;
