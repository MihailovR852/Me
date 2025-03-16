SELECT "Courier"."login", COUNT("Orders"."id") AS "in_delivery_orders"
FROM "Orders"
JOIN "Courier" ON "Orders"."courier_id" = "Courier"."id"
WHERE "Orders"."inDelivery" = TRUE
GROUP BY "Courier"."login";

SELECT "track", 
       CASE 
           WHEN "finished" = TRUE THEN 2
           WHEN "cancelled" = TRUE THEN -1
           WHEN "inDelivery" = TRUE THEN 1
           ELSE 0
       END AS "order_status"
FROM "Orders";