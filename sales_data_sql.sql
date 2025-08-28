CREATE TABLE sales (
    order_id TEXT,
    order_date DATE,
    product_category VARCHAR(100),
    region VARCHAR(100),
    quantity INT,
    price_per_unit DECIMAL(10,2),
    total_sales DECIMAL(12,2)
);
select*from sales limit 10;
select sum(case when order_date is null then 1 else 0 end)as missing_order_dates from sales ;
select sum(case when product_category is null then 1 else 0 end)as missing_product_category from sales;
select sum(case when total_sales is null then 1 else 0 end)as missing_total_sales from sales;
select date_format(order_date,'%y-%m')as month,sum(total_sales)as monthly_sales from sales group by month order by month ;
select product_category,sum(total_sales)as category_sales from sales group by product_category order by category_sales desc limit 5;
select region,count(*)as total_orders,sum(total_sales)as total_sales,avg(total_sales)as avg_order_value from sales group by region order by total_sales Desc;
