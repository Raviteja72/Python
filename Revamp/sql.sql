1
select b.booking_id, f.flight_name, 
subdate(b.booking_date,INTERVAL 5 Day) as PREPONED_DEPARTURE_DATE
from flight_details f 
join booking b on f.flight_id = b.flight_id 
where lower(f.flight_source) != 'miami'
order by b.booking_id desc;

2
select c.customer_id,c.customer_name,c.phone_no,
p.purchase_date
from customer_details c 
join purchase_details p on c.customer_id = p.customer_id
where lower(c.city) <> 'delhi'
order by c.customer_id desc;

3
select c.cust_name,o.order_id,o.order_date
from customers c 
join orders o on c.cust_id = o.cust_id 
where c.email_id like "%gmail%"
order by o.order_id desc;

4
select b1.boat_id, b1.boat_name
from boat_details b1 
join boat_details b2 on b1.seat_capacity = b2.seat_capacity 
where b1.boat_id <> b2.boat_id
order by b1.boat_name;

5
select distinct p.productname,p.category
from products p 
join feedback f on p.product_id = f.product_id
where f.rating_value < 3
order by p.productname;

6
select m.fullname, m.email, m.member_id, f.product_id
from members m 
join feedback f on m.member_id = f.member_id
where month(m.Date_of_birth) in (1,12)
order by m.fullname desc;

7
select c.cust_name,c.email_id,
colaesce(c.address,c.phone_no) as Contact_Info
from customers c
join orders o on c.cust_id = o.cust_id 
where o.order_date <> o.delivery_date
order by c.cust_name;

8
select m.movie_name, sm.theatre_id, m.duration
from movie_master m 
join screening_master sm on m.movie_id = sm.movie_id 
where lower(m.language) <> 'hindi'
order by m.movie_name desc;

9
select f1.flight_name, f1.flight_source 
from flight_details f1 
join flight_details f2 on f1.flight_destination = f2.flight_destination
and lower(f1.flight_destination) <> 'chicago' and
f1.flight_id <> f2.flight_id
order by f1.flight_destination, f1.flight_name;

10
select m.fullname
from members m 
join feedback f on m.member_id = f.member_id
where m.email like "%gmail%" 
and lower(m.address) = 'bangalore'
and f.rating_value > 4
order by m.fullname desc;

11
select p_first_name, a.app_reason, a.app_time,
b.bill_amount 
from patient p 
join appointment a on p.patient_id = a.patient_id
join bill b on a.app_number = b.app_number
where p.address like "%Avenue%"
order by a.app_time;

12
select distinct c.cust_name,c.email_id,c.phone_no 
from customers c 
join orders o on c.cust_id = o.cust_id
where month(o.order_date) in (2,3,4,5,6,7,8)
order by c.cust_name; // Between 2 and 8 

13
select b.boat_id, b.boat_name, b.boat_type,
round(b.seat_capacity-b.seat_capacity*0.25,2) as SEAT_COUNT
from boat_details b 
join ride_details r on b.boat_id = r.boat_id
where year(r.dot) = 2000
order by b.boat_name desc;

14
select m.movie_id, m.movie_name, sm.show_time
from movie_master m 
join screening_master sm on m.movie_id = sm.movie_id
where lower(m.language) = 'tamil' and m.certification <> 'A'
order by sm.screening_id desc;

15
select patient_id, p_first_name, p.city, p.p_age
from patient p 
join appointment a on p.patient_id = a.patient_id 
join bill b on a.app_number = b.app_number 
left join payment pt on b.bill_number = pt.bill_number
where pt.patient_id is null 
order by p.age;

where b.bill_number not in (select bill_number from payment)
order by p.p_age;

16
select c.customer_id, c.customer_name,
pe.policy_id, pe.total_amount, pe.no_of_years 
from customer c 
join policyenrollment pe on c.customer_id = oe.customer_id
where c.email_id like "%gmail%"
order by pe.enrollment_id desc;

17
select c.customer_id, c.customer_name, pe.policy_id
from customer c 
join policyenrollment pe on c.customer_id = pe.customer_id
where c.gender = 'M'
order by pe.enrollment_id desc;

18
select p.policy_id, p.policy_name
from policy p 
join policyenrollment pe on p.policy_id = pe.policy_id
group by pe.policy_id 
having sum(pe.no_of_years) = (
    select max(cnt) from (
        select sum(no_of_years) as cnt 
        from policyenrollment
        group by policy_id)tab
    )order by p.policy_name;

    select p.policy_id, p.policy_name
    from policy p
    where p.policy_id in (
        select policy_id from policyenrollment
        group by policy_id 
        having sum(no_of_years) = (
            select max(cnt) from (
                select policy_id,sum(no_of_years) as cnt from policyenrollment
                group by policy_id
            )tab1
        )tab2
    )order by p.policy_name;

19
select c.customer_name, bd.total_amount
from customer_master c 
join booking_details bd on c.customer_id = bd.customer_id
where year(bd.booking_details) = 2018
order by bd.booking_id desc;

20
select p1.p_first_name, p1.city
from patient p1 
join patient p2 on p1.city = p2.city 
where p1.patient_id <> p2.patient_id
order by p1.city,p1.p_first_name;

21
select c.customer_name 
from customer c 
join subscription s on c.phone_number = s.phone_number
group by c.phone_number
having s.recharge_date = (
    select max(recharge_date) from subscription) tab
order by c.customer_name desc;

select customer_name from customer 
where phone_number in (
    select phone_number from subscription
    where recharge_date = (
        select max(recharge_date) from subscription
    )
)order by customer_name desc;

22
c.customer_id, c.customer_name, c.date_of_birth,
c.marital_status, c.gender, c.guardian_name, c.contact_no, c.mail_id
from customer_personal_info c 
where upper(c.gender) = 'M' and upper(c.marital_status) = 'MARRIED'
order by c.customer_id;

23
select c.customer_id, a.account_no,
concat(right(c.customer_id,3),right(a.account_no,4)) as PASSCODE
from customer_personal_info c 
join account_info a on c.customer_id = a.customer_id
order by c.customer_id;

24
select c.customer_id, c.customer_name, c.date_of_birth, c.guardian_name
from customer_personal_info c 
where c.customer_name like "J%"
order by c.customer_id;

25
select c.customer_id, c.customer_name, a.account_no,
a.account_type, b.bank_name, b.ifsc_code, a.initial_deposit,
case
    when upper(a.account_type) = 'SAVINGS' then round(a.interest + a.interest*0.1,2)
    else a.interest
end as NEW_INTEREST
from customer_personal_info c 
join account_info a on c.customer_id = a.customer_id
join bank_info b on a.ifsc_code = b.ifsc_code
where c.customer_name like "J%"
order by c.customer_id;

26
select c.customer_id, c.customer_name,
a.account_no, a.initial_deposit,
case    
    when a.initial_deposit = 0 then '0%'
    when a.initial_deposit <= 10000 then '3%'
    when a.initial_deposit > 10000 and a.initial_deposit < 20000 then '5%'
    when a.initial_deposit>= 20000 and a.initial_deposit <= 30000 then '7%'
    when a.initial_deposit > 30000 then '10%'
end as taxPercentage
from customer_personal_info c 
join account_info a on c.customer_id = a.customer_id
order by c.customer_id;

27
select a.customer_id, a.account_type, a.account_no,b.bank_name

28
c.customer_id, c.customer_name,
c.guardian_name, r.reference_acc_name
from customer_personal_info c 
join customer_reference_info r on c.customer_id = r.customer_id
where lower(r.relation) = 'friend'
order by c.customer_id;

29
select c.customer_id, a.account_no, 
concat('$',round(a.interest,0)) as INTEREST_AMT
from c and a 
order by a.interest, c.customer_id

30
where a.activate_date = '2012-04-10'

31

32
where lower(c.identification_doc_type) = 'passport'

33

34
concat(customer_name,'_',gender,'_',marital_status) as UNIQUE_REF_STRING

35
where initial_deposit between 15000 and 25000

36
round(a.initial_deposit + a.interest,0) as current_balance
where upper(a.account_type) = 'SAVINGS'

37
(activate_date - registration_date) as NoofdaysforActivation

38
select a.customer_id, a.account_type, a.account_no
from account_info a 
join bank_info b on a.ifsc_code = b.ifsc_code
where upper(b.bank_name) = 'HDFC' and 
a.registration_date between '2012-01-12' and '2012-04-04'
order by c.customer_id;

39
concat('+91',substr(c.contact_no,1,3),'-',substr(c.contact_no,4,3),'-',substr(c.contact_no,7)) as CONTACT_ISD

40
select c.customer_id, c.customer_name,
c.dob, c.guardian_name, c.contact_no,
c.mail_id,r.reference_acc_name 
from customer_personal_info c 
join customer_reference_info r on c.customer_id = r.customer_id
where r.customer_id = (
    select customer_id from customer_personal_info
    where upper(customer_name) = 'RAGHUL'
)tab
order by c.csutomer_id

41
where upper(c.address) = 'BANGALORE'

42
case
    when initial_deposit = 20000 then 'high'
    when initial_deposit = 16000 then 'moderate'
    when initial_deposit = 10000 then 'average'
    when initial_deposit = 5000 then 'low'
    when initial_deposit = 0 then 'very low'
    else 'invalid'
end as Deposit_Status

43
select c.customer_id, c.customer_name, 
a.account_no, a.account_type, b.bank_name, a.initial_deposit
where a.interest = (
    select max(interest) 
    from account_info 
    -- group by account_no
)
order by c.customer_id;

44
select c.customer_id, c.customer_name, a.account_type,
a.initial_deposit, a.interest 
from customer_personal_info c 
join account_info a on c.customer_id = a.csutomer_id
where a.initial_deposit = (
    select max(initial_deposit) from account_info
)
order by c.csutomer_id;

45
where month(activate_date) = 3

46
((interest/100)*initial_deposit) as interest_amt
