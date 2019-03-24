CREATE or REPLACE FUNCTION insert_cust_func() RETURNS trigger AS $insert_cust_func$
  BEGIN
    IF TG_OP = 'INSERT' THEN
      INSERT INTO newcustomers VALUES (NEW.customerid, NEW.name, NEW.birthdate);
      IF NEW.frequentflieron IS not NULL THEN
        --cascades
        INSERT INTO ffairlines VALUES (NEW.customerid, NEW.frequentflieron);
      END IF;

    ELSIF TG_OP = 'UPDATE' THEN
      UPDATE newcustomers SET name = NEW.name, birthdate = NEW.birthdate WHERE customerid = OLD.customerid;
      IF NEW.frequentflieron IS NULL THEN
        DELETE FROM ffairlines WHERE customerid = OLD.customerid;
      ELSIF NEW.frequentflieron IS NOT NULL Then
        IF NOT EXISTS (select * from ffairlines where customerid = OLD.customerid AND airlineid = NEW.frequentflieron) then
          INSERT INTO ffairlines VALUES (OLD.customerid, NEW.frequentflieron);
        END IF;
      END IF;

    ELSIF TG_OP = 'DELETE' THEN
      DELETE FROM newcustomers WHERE customerid = OLD.customerid;
    END IF;
    return null;
  END;
$insert_cust_func$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION insert_new_func() RETURNS trigger AS $insert_new_func$
  BEGIN
    IF TG_OP = 'INSERT' THEN
      INSERT INTO customers VALUES (NEW.customerid, NEW.name, NEW.birthdate, null);

    ELSIF TG_OP = 'UPDATE' THEN
      UPDATE customers SET name = NEW.name, birthdate = NEW.birthdate WHERE customerid = OLD.customerid;
    ELSIF TG_OP = 'DELETE' THEN
      DELETE FROM customers WHERE customerid = OLD.customerid;
    END IF;
    return null;
  END;
$insert_new_func$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION airline() RETURNS trigger AS $airline$
  BEGIN
    IF TG_OP = 'INSERT' THEN
      UPDATE customers
      SET frequentflieron =
      (with temp(id, value) as (select m.airlineid, count(x.flightid)
        from flewon x, flights y, customers z, ffairlines m
        where m.airlineid = y.airlineid AND x.flightid = y.flightid and z.customerid = x.customerid and z.customerid = NEW.customerid
        group by m.airlineid)
        select id from temp where value = (select max(value) from temp) limit 1)
      WHERE customerid = NEW.customerid;
    ELSIF TG_OP = 'UPDATE' OR TG_OP = 'DELETE' THEN
      UPDATE customers
      SET frequentflieron =
      (with temp(id, value) as (select m.airlineid, count(x.flightid)
        from flewon x, flights y, customers z, ffairlines m
        where m.airlineid = y.airlineid AND x.flightid = y.flightid and z.customerid = x.customerid and z.customerid = OLD.customerid
        group by m.airlineid)
        select id from temp where value = (select max(value) from temp) limit 1)
      WHERE customerid = OLD.customerid;
    END IF;
    return null;
  End;
$airline$ LANGUAGE plpgsql;

CREATE or REPLACE FUNCTION flewon_change() RETURNS trigger AS $flewon_change$
  BEGIN
    IF TG_OP = 'INSERT' THEN
      UPDATE customers
      SET frequentflieron =
      (with temp(id, value) as (select m.airlineid, count(x.flightid)
        from flewon x, flights y, customers z, ffairlines m
        where m.airlineid = y.airlineid AND x.flightid = y.flightid and z.customerid = x.customerid and z.customerid = NEW.customerid
        group by m.airlineid)
        select id from temp where value = (select max(value) from temp) limit 1)
      WHERE customerid = NEW.customerid;
    ELSIF TG_OP = 'UPDATE' OR TG_OP = 'DELETE' THEN
      UPDATE customers
      SET frequentflieron =
      (with temp(id, value) as (select m.airlineid, count(x.flightid)
        from flewon x, flights y, customers z, ffairlines m
        where m.airlineid = y.airlineid AND x.flightid = y.flightid and z.customerid = x.customerid and z.customerid = OLD.customerid
        group by m.airlineid)
        select id from temp where value = (select max(value) from temp) limit 1)
      WHERE customerid = OLD.customerid;
    END IF;
    return null;
  End;
$flewon_change$ LANGUAGE plpgsql;




CREATE TRIGGER insert_cust_func
AFTER INSERT OR UPDATE OR DELETE ON customers
    FOR EACH ROW WHEN (pg_trigger_depth() = 0)
    EXECUTE PROCEDURE insert_cust_func();

CREATE TRIGGER insert_new_func
AFTER INSERT OR UPDATE OR DELETE ON newcustomers
    FOR EACH ROW WHEN (pg_trigger_depth() = 0)
    EXECUTE PROCEDURE insert_new_func();

CREATE TRIGGER airline
AFTER INSERT OR UPDATE OR DELETE ON ffairlines
  FOR EACH ROW WHEN (pg_trigger_depth() <= 1)
  EXECUTE PROCEDURE airline();

CREATE TRIGGER flewon_change
AFTER INSERT OR UPDATE OR DELETE ON flewon
    FOR EACH ROW WHEN (pg_trigger_depth() = 0)
    EXECUTE PROCEDURE flewon_change();
