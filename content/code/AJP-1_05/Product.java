public class Product {
	private String brand;
	private String model;
	private double price;
	
	public String getBrand() {
		return brand;
	}
	
	public void setBrand(String brand) {
		this.brand = brand;
	}
	
	public String getModel() {
		return model;
	}
	
	public void setModel(String model) {
		this.model = model;
	}
	
	public double getPrice() {
		return price;
	}
	
	public void setPrice(double price) {
		this.price = price;
	}
	
	public Product() {
	}
	
	public Product(String brand, String model) {
		this.brand = brand;
		this.model = model;
	}
	
	public Product(String brand, String model, double price) {
		this.brand = brand;
		this.model = model;
		this.price = price;
	}
	
	@Override
	public String toString() {
		return "Brand='" + this.brand + "', model='" + this.model + "', price=" + this.price;
	}
}