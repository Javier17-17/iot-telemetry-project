--
-- PostgreSQL database dump
--

\restrict Rm4mycvKzS7QMTVwh3tzKFAJh2hAbUSgWBHqlnHyhL8TBbd14Dk417qsENioiKT

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-05-26 11:11:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 24618)
-- Name: alarms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alarms (
    id integer NOT NULL,
    device_id integer,
    alarm_type character varying(50),
    value double precision,
    message text,
    "timestamp" timestamp without time zone NOT NULL
);


ALTER TABLE public.alarms OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 24617)
-- Name: alarms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alarms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.alarms_id_seq OWNER TO postgres;

--
-- TOC entry 5043 (class 0 OID 0)
-- Dependencies: 225
-- Name: alarms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alarms_id_seq OWNED BY public.alarms.id;


--
-- TOC entry 222 (class 1259 OID 24598)
-- Name: devices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.devices (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    type character varying(50) NOT NULL,
    location character varying(100)
);


ALTER TABLE public.devices OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24597)
-- Name: devices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.devices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.devices_id_seq OWNER TO postgres;

--
-- TOC entry 5044 (class 0 OID 0)
-- Dependencies: 221
-- Name: devices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.devices_id_seq OWNED BY public.devices.id;


--
-- TOC entry 224 (class 1259 OID 24608)
-- Name: scale_events; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scale_events (
    id integer NOT NULL,
    weight double precision NOT NULL,
    truck_plate character varying(20),
    "timestamp" timestamp without time zone NOT NULL
);


ALTER TABLE public.scale_events OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 24607)
-- Name: scale_events_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.scale_events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.scale_events_id_seq OWNER TO postgres;

--
-- TOC entry 5045 (class 0 OID 0)
-- Dependencies: 223
-- Name: scale_events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.scale_events_id_seq OWNED BY public.scale_events.id;


--
-- TOC entry 220 (class 1259 OID 24586)
-- Name: telemetry; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.telemetry (
    id integer NOT NULL,
    device_id integer NOT NULL,
    temperature double precision NOT NULL,
    humidity double precision NOT NULL,
    "timestamp" timestamp without time zone NOT NULL
);


ALTER TABLE public.telemetry OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24585)
-- Name: telemetry_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.telemetry_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.telemetry_id_seq OWNER TO postgres;

--
-- TOC entry 5046 (class 0 OID 0)
-- Dependencies: 219
-- Name: telemetry_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.telemetry_id_seq OWNED BY public.telemetry.id;


--
-- TOC entry 4874 (class 2604 OID 24621)
-- Name: alarms id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alarms ALTER COLUMN id SET DEFAULT nextval('public.alarms_id_seq'::regclass);


--
-- TOC entry 4872 (class 2604 OID 24601)
-- Name: devices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices ALTER COLUMN id SET DEFAULT nextval('public.devices_id_seq'::regclass);


--
-- TOC entry 4873 (class 2604 OID 24611)
-- Name: scale_events id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scale_events ALTER COLUMN id SET DEFAULT nextval('public.scale_events_id_seq'::regclass);


--
-- TOC entry 4871 (class 2604 OID 24589)
-- Name: telemetry id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telemetry ALTER COLUMN id SET DEFAULT nextval('public.telemetry_id_seq'::regclass);


--
-- TOC entry 5037 (class 0 OID 24618)
-- Dependencies: 226
-- Data for Name: alarms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alarms (id, device_id, alarm_type, value, message, "timestamp") FROM stdin;
1	1	HIGH_TEMPERATURE	29.5	Temperatura demasiado alta	2026-05-21 13:45:00
2	1	HIGH_HUMIDITY	66	Humedad demasiado alta	2026-05-21 13:45:00
3	1	HIGH_TEMPERATURE	29.5	Temperatura demasiado alta	2026-05-21 13:45:00
4	1	HIGH_HUMIDITY	66	Humedad demasiado alta	2026-05-21 13:45:00
\.


--
-- TOC entry 5033 (class 0 OID 24598)
-- Dependencies: 222
-- Data for Name: devices; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.devices (id, name, type, location) FROM stdin;
1	Sensor Secadero 1	temperature_humidity	Secadero principal
2	Sensor Secadero 2	temperature_humidity	Secadero secundario
\.


--
-- TOC entry 5035 (class 0 OID 24608)
-- Dependencies: 224
-- Data for Name: scale_events; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.scale_events (id, weight, truck_plate, "timestamp") FROM stdin;
1	1250.5	1234ABC	2026-05-21 14:05:00
\.


--
-- TOC entry 5031 (class 0 OID 24586)
-- Dependencies: 220
-- Data for Name: telemetry; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.telemetry (id, device_id, temperature, humidity, "timestamp") FROM stdin;
1	1	12	20	2026-04-24 11:20:13.159
2	1	12	20	2026-04-24 11:20:13.159
3	1	26.88	65.62	2026-04-24 11:22:16.680745
4	1	26.27	46.03	2026-04-24 11:22:21.827887
5	1	26.3	50.42	2026-04-24 11:22:26.896989
6	1	20.91	42.25	2026-04-24 11:22:32.009957
7	1	22.64	40.99	2026-04-24 11:22:37.108389
8	1	29.37	50.47	2026-04-24 11:22:42.203428
9	1	29.18	45.79	2026-04-24 11:22:47.28754
10	1	27.32	50.62	2026-04-24 11:22:52.404993
11	1	25.84	50.98	2026-04-24 11:22:57.500835
12	1	23.15	64.5	2026-04-24 11:23:02.579907
13	1	27.44	56.35	2026-04-24 11:23:07.67052
14	1	28.38	40.09	2026-04-24 11:23:12.761847
15	1	25.32	63.56	2026-04-24 11:23:17.857672
16	1	21.87	58.24	2026-04-24 11:23:22.934125
17	1	25.6	61.91	2026-04-24 11:23:28.017884
18	1	25.99	60.84	2026-04-24 11:23:33.107447
19	1	24.87	52.83	2026-04-24 11:23:38.215831
20	1	24.45	60.7	2026-04-24 11:23:43.341345
21	1	26.2	48.37	2026-04-24 11:23:48.446919
22	1	25.9	45.62	2026-04-24 11:23:53.550343
23	1	29.78	62.22	2026-04-24 11:23:58.654672
24	1	23.89	44.78	2026-04-24 11:24:03.741495
25	1	21.07	48.45	2026-04-24 11:24:08.831318
26	1	29.17	69.16	2026-04-24 11:24:13.910574
27	1	29.13	40.97	2026-04-24 11:24:18.996509
28	1	25.77	65.54	2026-04-24 11:24:24.085373
29	1	28.6	44.72	2026-04-24 11:24:29.179244
30	1	26.38	56.06	2026-04-24 11:24:34.38452
31	1	29.41	52.14	2026-04-24 11:24:39.472186
32	1	21.1	59.67	2026-04-24 11:24:44.578397
33	1	27.41	58.48	2026-04-24 11:24:49.676827
34	1	25.07	42.87	2026-04-24 11:24:54.765243
35	1	20.57	57.41	2026-04-24 11:24:59.845611
36	1	22.57	41.65	2026-04-24 11:25:04.933402
37	1	20.07	44.95	2026-04-24 11:25:10.02044
38	1	24.8	64.41	2026-04-24 11:25:15.111173
39	1	29.34	58.8	2026-04-24 11:25:20.210458
40	1	21.33	66.41	2026-04-24 11:25:25.298459
41	1	28.16	40.22	2026-04-24 11:25:30.382426
42	1	21.89	45.56	2026-04-24 11:25:35.472494
43	1	23.59	42.97	2026-04-24 11:25:40.55592
44	1	29.56	56.17	2026-04-24 11:25:45.638712
45	1	28.13	43.35	2026-04-24 11:25:50.73133
46	1	21.51	43.03	2026-04-24 11:25:55.81964
47	1	21.42	43.5	2026-04-24 11:26:00.909873
48	1	23.1	45.47	2026-04-24 11:26:06.001178
49	1	25.33	66.52	2026-04-24 11:26:11.119577
50	1	22.06	46.99	2026-04-24 11:26:16.22396
51	1	23.45	68.03	2026-04-24 11:26:21.32702
52	1	28.03	57.21	2026-04-24 11:26:26.429384
53	1	28.84	47.09	2026-04-24 11:26:31.523675
54	1	28.26	57.46	2026-04-24 11:26:36.626465
55	1	24.88	47.62	2026-04-24 11:26:41.720721
56	1	28.82	49.68	2026-04-24 11:26:46.820707
57	1	23.3	45.76	2026-04-24 11:26:51.909571
58	1	29.5	66	2026-05-21 13:45:00
59	1	29.5	66	2026-05-21 13:45:00
\.


--
-- TOC entry 5047 (class 0 OID 0)
-- Dependencies: 225
-- Name: alarms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.alarms_id_seq', 4, true);


--
-- TOC entry 5048 (class 0 OID 0)
-- Dependencies: 221
-- Name: devices_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.devices_id_seq', 2, true);


--
-- TOC entry 5049 (class 0 OID 0)
-- Dependencies: 223
-- Name: scale_events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.scale_events_id_seq', 1, true);


--
-- TOC entry 5050 (class 0 OID 0)
-- Dependencies: 219
-- Name: telemetry_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.telemetry_id_seq', 59, true);


--
-- TOC entry 4882 (class 2606 OID 24627)
-- Name: alarms alarms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alarms
    ADD CONSTRAINT alarms_pkey PRIMARY KEY (id);


--
-- TOC entry 4878 (class 2606 OID 24606)
-- Name: devices devices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.devices
    ADD CONSTRAINT devices_pkey PRIMARY KEY (id);


--
-- TOC entry 4880 (class 2606 OID 24616)
-- Name: scale_events scale_events_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.scale_events
    ADD CONSTRAINT scale_events_pkey PRIMARY KEY (id);


--
-- TOC entry 4876 (class 2606 OID 24596)
-- Name: telemetry telemetry_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.telemetry
    ADD CONSTRAINT telemetry_pkey PRIMARY KEY (id);


-- Completed on 2026-05-26 11:11:28

--
-- PostgreSQL database dump complete
--

\unrestrict Rm4mycvKzS7QMTVwh3tzKFAJh2hAbUSgWBHqlnHyhL8TBbd14Dk417qsENioiKT

