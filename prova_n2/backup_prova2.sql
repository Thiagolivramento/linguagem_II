PGDMP                      
    x            prova #   11.7 (Ubuntu 11.7-0ubuntu0.19.10.1) #   11.7 (Ubuntu 11.7-0ubuntu0.19.10.1) 	    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    16561    prova    DATABASE     w   CREATE DATABASE prova WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8';
    DROP DATABASE prova;
             postgres    false            �            1259    16562    musica    TABLE     �   CREATE TABLE public.musica (
    id bigint NOT NULL,
    nome character varying(250) NOT NULL,
    autoria character varying(250) NOT NULL,
    genero character varying(250) NOT NULL
);
    DROP TABLE public.musica;
       public         postgres    false            �            1259    16570    pessoa    TABLE     �   CREATE TABLE public.pessoa (
    nome character varying NOT NULL,
    cpf character varying NOT NULL,
    email character varying NOT NULL,
    deletado character varying
);
    DROP TABLE public.pessoa;
       public         postgres    false            |          0    16562    musica 
   TABLE DATA               ;   COPY public.musica (id, nome, autoria, genero) FROM stdin;
    public       postgres    false    196   �       }          0    16570    pessoa 
   TABLE DATA               <   COPY public.pessoa (nome, cpf, email, deletado) FROM stdin;
    public       postgres    false    197   �                  2606    16569    musica Musica_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.musica
    ADD CONSTRAINT "Musica_pkey" PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.musica DROP CONSTRAINT "Musica_pkey";
       public         postgres    false    196            |   ?   x�3�� �"�L.#�r�L�D �2��H�A�$0 ����	g	@��W����� �@!      }   ?   x��HL�I,�406ճ44�3���33�L-��)�.��10uH�M���K���LK�)N����� ���     