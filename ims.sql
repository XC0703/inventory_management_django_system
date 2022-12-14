--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: app_cart; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_cart (
    id integer NOT NULL,
    "cartId" character varying(20) NOT NULL,
    "userId" character varying(20) NOT NULL,
    "userName" character varying(15) NOT NULL,
    "wareId" character varying(20) NOT NULL,
    "wareName" character varying(15) NOT NULL,
    "wareCount" numeric(10,0) NOT NULL,
    "createTime" timestamp with time zone NOT NULL,
    "updateTime" timestamp with time zone NOT NULL
);


ALTER TABLE public.app_cart OWNER TO postgres;

--
-- Name: app_cart_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_cart ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_cart_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_order (
    id integer NOT NULL,
    "orderId" character varying(20) NOT NULL,
    "userId" character varying(20) NOT NULL,
    "userName" character varying(15) NOT NULL,
    "wareId" character varying(20) NOT NULL,
    "wareName" character varying(15) NOT NULL,
    "wareCount" numeric(10,0) NOT NULL,
    "createTime" timestamp with time zone NOT NULL
);


ALTER TABLE public.app_order OWNER TO postgres;

--
-- Name: app_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_order ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_sales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_sales (
    id integer NOT NULL,
    "salesId" character varying(20) NOT NULL,
    "yearName" character varying(5) NOT NULL,
    "yearSales" numeric(10,2) NOT NULL,
    "yearEvents" character varying(30) NOT NULL,
    "monthSales" jsonb,
    "wareSales" jsonb
);


ALTER TABLE public.app_sales OWNER TO postgres;

--
-- Name: app_sales_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_sales ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_sales_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_user (
    id integer NOT NULL,
    "userId" character varying(20) NOT NULL,
    "userName" character varying(15) NOT NULL,
    "userPassword" character varying(20) NOT NULL,
    "userPower" numeric(3,0) NOT NULL,
    "createTime" timestamp with time zone NOT NULL,
    "updateTime" timestamp with time zone NOT NULL
);


ALTER TABLE public.app_user OWNER TO postgres;

--
-- Name: app_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: app_ware; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_ware (
    id integer NOT NULL,
    "wareId" character varying(20) NOT NULL,
    "wareName" character varying(15) NOT NULL,
    "warePower" numeric(8,0) NOT NULL,
    "wareCount" numeric(10,0) NOT NULL,
    "createTime" timestamp with time zone NOT NULL,
    "updateTime" timestamp with time zone NOT NULL
);


ALTER TABLE public.app_ware OWNER TO postgres;

--
-- Name: app_ware_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.app_ware ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.app_ware_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Data for Name: app_cart; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_cart (id, "cartId", "userId", "userName", "wareId", "wareName", "wareCount", "createTime", "updateTime") FROM stdin;
1	cart000001	user000001	scucsyyds	ware000001	一眼丁真	114514	2022-12-02 09:37:32.978608+08	2022-12-02 09:37:32.978608+08
2	cart000002	user000001	scucsyyds	ware000001	一眼丁真	114	2022-12-02 09:37:51.629743+08	2022-12-02 09:37:51.629743+08
4	cart000004	user000003	yydzyyds	ware000001	一眼丁真	11111	2022-12-02 09:40:02.198642+08	2022-12-02 09:40:02.198642+08
6	cart000006	user000003	yydzyyds	ware000001	一眼丁真	89	2022-12-02 10:15:27.68774+08	2022-12-02 10:15:27.68774+08
8	cart000008	user000003	yydzyyds	ware000001	一眼丁真	89	2022-12-02 10:19:04.820287+08	2022-12-02 10:19:04.820287+08
9	cart000009	user000005	mm	ware000002	显示屏	3	2022-12-04 14:02:39.340802+08	2022-12-04 14:02:39.340802+08
3	cart000003	user000001	scucsyyds	ware000001	一眼丁真	512	2022-12-02 09:37:57.474724+08	2022-12-02 09:37:57.474724+08
10	cart000010	user000004	csyyds	ware000002	显示屏	3	2022-12-04 14:05:48.547534+08	2022-12-04 14:05:48.547534+08
11	cart000011	user000004	csyyds	ware000004	书本	3	2022-12-04 14:06:35.979051+08	2022-12-04 14:06:35.979051+08
\.


--
-- Data for Name: app_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_order (id, "orderId", "userId", "userName", "wareId", "wareName", "wareCount", "createTime") FROM stdin;
1	order000001	user000004	lcyyds	ware000001	键盘	3	2022-12-03 23:13:03.394097+08
2	order000002	user000004	lcyyds	ware000001	键盘	3	2022-12-03 23:29:09.482564+08
3	order000003	user000004	lcyyds	ware000001	键盘	2	2022-12-03 23:30:47.47198+08
4	order000004	user000004	lcyyds	ware000001	键盘	4	2022-12-03 23:55:27.071402+08
6	order000006	user000004	lcyyds	ware000001	键盘	3	2022-12-03 23:56:10.577331+08
7	order000007	user000004	lcyyds	ware000001	键盘	3	2022-12-04 00:39:06.239103+08
8	order000008	user000003	yydzyyds	ware000001	一眼丁真	2222	2022-12-04 10:42:16.411424+08
10	order000010	user000003	yydzyyds	ware000001	一眼丁真	89	2022-12-04 10:42:30.840029+08
11	order000011	user000005	mm	ware000003	鼠标	3	2022-12-04 14:02:20.851437+08
12	order000012	user000003	yydzyyds	ware000001	一眼丁真	89	2022-12-04 14:02:57.228571+08
13	order000013	user000004	csyyds	ware000004	书本	3	2022-12-04 14:06:54.972927+08
\.


--
-- Data for Name: app_sales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_sales (id, "salesId", "yearName", "yearSales", "yearEvents", "monthSales", "wareSales") FROM stdin;
1	sales000001	2012	79.54		[0.24, 0.3, 2, 2, 5, 9, 10, 14, 7, 10, 9, 8]	[{"name": "物品1", "value": 26.5, "salesVolume": 7}, {"name": "物品2", "value": 24.41, "salesVolume": 6}, {"name": "物品3", "value": 20.54, "salesVolume": 8}, {"name": "物品4", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
2	sales000002	2013	64.44	公司重组	[0.44, 3, 5, 2, 3, 4, 11, 13, 3, 5, 7, 2, 6]	[{"name": "物品3", "value": 24.5, "salesVolume": 6}, {"name": "物品7", "value": 24.41, "salesVolume": 9}, {"name": "物品6", "value": 20.54, "salesVolume": 8}, {"name": "物品3", "value": 12.77, "salesVolume": 5}, {"name": "物品3", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
3	sales000003	2014	80.00		[0.54, 3.3, 5.7, 2.9, 5.3, 6, 16, 12, 10, 4.8, 8.2, 5.6]	[{"name": "物品1", "value": 27.5, "salesVolume": 7}, {"name": "物品2", "value": 24.41, "salesVolume": 6}, {"name": "物品3", "value": 18.54, "salesVolume": 8}, {"name": "物品4", "value": 14.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 0.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
4	sales000004	2015	75.00		[0.54, 4.5, 3, 2, 5, 9, 13, 11, 7, 1, 10, 8]	[{"name": "物品7", "value": 28.5, "salesVolume": 7}, {"name": "物品4", "value": 20.41, "salesVolume": 6}, {"name": "物品3", "value": 18.54, "salesVolume": 8}, {"name": "物品2", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品2", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
5	sales000005	2016	90.00		[0.64, 7.6, 1, 3, 5, 9, 9, 12, 6, 13, 1, 6]	[{"name": "物品1", "value": 28.5, "salesVolume": 7}, {"name": "物品2", "value": 25.41, "salesVolume": 6}, {"name": "物品5", "value": 20.54, "salesVolume": 8}, {"name": "物品6", "value": 6.77, "salesVolume": 8}, {"name": "物品3", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
6	sales000006	2017	87.00		[0.74, 6.7, 3, 4, 5, 9, 8, 19, 6, 12, 12, 5]	[{"name": "物品9", "value": 29.5, "salesVolume": 7}, {"name": "物品6", "value": 26.41, "salesVolume": 6}, {"name": "物品3", "value": 24.54, "salesVolume": 8}, {"name": "物品4", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品2", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品1", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
7	sales000007	2018	65.00	公司改革	[1.24, 7.9, 6, 4, 5, 9, 14, 12, 4, 13, 10, 2]	[{"name": "物品6", "value": 20.5, "salesVolume": 7}, {"name": "物品2", "value": 15.41, "salesVolume": 6}, {"name": "物品3", "value": 14.54, "salesVolume": 10}, {"name": "物品6", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品4", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
8	sales000008	2019	97.00		[2.24, 3.7, 3, 7, 5, 9, 12, 14, 8, 11, 12, 4]	[{"name": "物品1", "value": 26.5, "salesVolume": 7}, {"name": "物品2", "value": 24.41, "salesVolume": 6}, {"name": "物品3", "value": 20.54, "salesVolume": 8}, {"name": "物品4", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
9	sales000009	2020	87.00	新冠疫情开始	[3.24, 2.3, 7, 5, 5, 10, 13, 16, 9, 12, 2, 8]	[{"name": "物品1", "value": 30.5, "salesVolume": 7}, {"name": "物品5", "value": 26.41, "salesVolume": 8}, {"name": "物品3", "value": 17.54, "salesVolume": 8}, {"name": "物品4", "value": 12.77, "salesVolume": 8}, {"name": "物品2", "value": 5.14, "salesVolume": 6}, {"name": "物品6", "value": 3.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
10	sales000010	2021	90.00		[1.24, 4.5, 4, 2, 5, 9, 11, 19, 10, 13, 12, 7]	[{"name": "物品1", "value": 26.5, "salesVolume": 7}, {"name": "物品2", "value": 24.41, "salesVolume": 6}, {"name": "物品3", "value": 20.54, "salesVolume": 8}, {"name": "物品4", "value": 12.77, "salesVolume": 8}, {"name": "物品5", "value": 4.14, "salesVolume": 6}, {"name": "物品6", "value": 2.95, "salesVolume": 4}, {"name": "物品7", "value": 1.93, "salesVolume": 2}, {"name": "物品8", "value": 1.51, "salesVolume": 1}, {"name": "物品9", "value": 1.36, "salesVolume": 4}, {"name": "物品10", "value": 1.31, "salesVolume": 6}, {"name": "其它物品", "value": 0.93, "salesVolume": 1}]
\.


--
-- Data for Name: app_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_user (id, "userId", "userName", "userPassword", "userPower", "createTime", "updateTime") FROM stdin;
1	user000001	scucsyyds	123456	13	2022-12-02 09:21:41.686416+08	2022-12-02 09:21:41.686416+08
5	user000005	mm	123456	200	2022-12-04 00:50:59.657892+08	2022-12-04 00:50:59.657892+08
4	user000004	csyyds	csyyds	25	2022-12-03 17:34:42.548595+08	2022-12-03 17:34:42.548595+08
2	user000002	scuyyds	123456	15	2022-12-02 09:22:48.603693+08	2022-12-02 09:22:48.603693+08
6	user000006	lcyyds	lcyyds	10	2022-12-04 14:09:24.782341+08	2022-12-04 14:09:24.782341+08
\.


--
-- Data for Name: app_ware; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_ware (id, "wareId", "wareName", "warePower", "wareCount", "createTime", "updateTime") FROM stdin;
3	ware000003	鼠标	3434	30	2022-12-04 14:02:06.107868+08	2022-12-04 14:02:06.107868+08
1	ware000001	键盘	22	908	2022-12-03 22:16:41.064821+08	2022-12-03 22:16:41.064821+08
2	ware000002	显示屏	33	18	2022-12-03 23:46:57.996126+08	2022-12-03 23:46:57.996126+08
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add cart	7	add_cart
26	Can change cart	7	change_cart
27	Can delete cart	7	delete_cart
28	Can view cart	7	view_cart
29	Can add order	8	add_order
30	Can change order	8	change_order
31	Can delete order	8	delete_order
32	Can view order	8	view_order
33	Can add sales	9	add_sales
34	Can change sales	9	change_sales
35	Can delete sales	9	delete_sales
36	Can view sales	9	view_sales
37	Can add user	10	add_user
38	Can change user	10	change_user
39	Can delete user	10	delete_user
40	Can view user	10	view_user
41	Can add ware	11	add_ware
42	Can change ware	11	change_ware
43	Can delete ware	11	delete_ware
44	Can view ware	11	view_ware
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	app	cart
8	app	order
9	app	sales
10	app	user
11	app	ware
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-12-02 08:31:49.493026+08
2	auth	0001_initial	2022-12-02 08:31:49.684718+08
3	admin	0001_initial	2022-12-02 08:31:49.74005+08
4	admin	0002_logentry_remove_auto_add	2022-12-02 08:31:49.758038+08
5	admin	0003_logentry_add_action_flag_choices	2022-12-02 08:31:49.773721+08
6	app	0001_initial	2022-12-02 08:31:49.878243+08
7	contenttypes	0002_remove_content_type_name	2022-12-02 08:31:49.917226+08
8	auth	0002_alter_permission_name_max_length	2022-12-02 08:31:49.935578+08
9	auth	0003_alter_user_email_max_length	2022-12-02 08:31:49.952563+08
10	auth	0004_alter_user_username_opts	2022-12-02 08:31:49.970204+08
11	auth	0005_alter_user_last_login_null	2022-12-02 08:31:49.990501+08
12	auth	0006_require_contenttypes_0002	2022-12-02 08:31:49.995846+08
13	auth	0007_alter_validators_add_error_messages	2022-12-02 08:31:50.014268+08
14	auth	0008_alter_user_username_max_length	2022-12-02 08:31:50.047323+08
15	auth	0009_alter_user_last_name_max_length	2022-12-02 08:31:50.066326+08
16	auth	0010_alter_group_name_max_length	2022-12-02 08:31:50.089328+08
17	auth	0011_update_proxy_permissions	2022-12-02 08:31:50.114002+08
18	auth	0012_alter_user_first_name_max_length	2022-12-02 08:31:50.133023+08
19	sessions	0001_initial	2022-12-02 08:31:50.172096+08
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: app_cart_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_cart_id_seq', 11, true);


--
-- Name: app_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_order_id_seq', 13, true);


--
-- Name: app_sales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_sales_id_seq', 10, true);


--
-- Name: app_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_user_id_seq', 6, true);


--
-- Name: app_ware_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_ware_id_seq', 4, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, false);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: app_cart app_cart_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_cart
    ADD CONSTRAINT app_cart_pkey PRIMARY KEY (id);


--
-- Name: app_order app_order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_order
    ADD CONSTRAINT app_order_pkey PRIMARY KEY (id);


--
-- Name: app_sales app_sales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_sales
    ADD CONSTRAINT app_sales_pkey PRIMARY KEY (id);


--
-- Name: app_user app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_user
    ADD CONSTRAINT app_user_pkey PRIMARY KEY (id);


--
-- Name: app_user app_user_userName_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_user
    ADD CONSTRAINT "app_user_userName_key" UNIQUE ("userName");


--
-- Name: app_ware app_ware_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_ware
    ADD CONSTRAINT app_ware_pkey PRIMARY KEY (id);


--
-- Name: app_ware app_ware_wareName_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_ware
    ADD CONSTRAINT "app_ware_wareName_key" UNIQUE ("wareName");


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: app_user_userName_2f5ea20c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "app_user_userName_2f5ea20c_like" ON public.app_user USING btree ("userName" varchar_pattern_ops);


--
-- Name: app_ware_wareName_d5286fac_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "app_ware_wareName_d5286fac_like" ON public.app_ware USING btree ("wareName" varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--
