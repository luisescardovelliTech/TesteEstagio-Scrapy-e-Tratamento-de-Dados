create database testeestagio;

create table clientes( 
idCliente integer auto_increment not null primary key,
nome varchar(30) not null, 
email varchar(45)
);  

create table pedidos (
idPedido integer auto_increment not null primary key,
idCliente integer,  
dataPedido DATE,
total DECIMAL,
foreign key (idCliente) references clientes(idCliente)
);

select * from clientes;

insert into clientes (nome, email)
values 
('João Silva', 'joao@email.com'),
('Maria de Souza', 'maria@email.com'),
('Carlos Alberto', 'carlos@email.com');

select * from clientes;

select * from pedidos;

insert into pedidos (idCliente, dataPedido, total)
values
(1, '2025-05-01', 150.00),
(2, '2025-05-03', 70),
(3, '2025-05-07', 120.50);

select clientes.nome "Nome do Cliente",
	pedidos.total "Valores"
from pedidos
join clientes on pedidos.idCliente = clientes.idCliente
where pedidos.total > 100
order by clientes.nome;

select 
    clientes.nome "Nome do Cliente",
    COUNT(pedidos.idPedido) "Total de Pedidos"
from clientes
join pedidos on pedidos.idCliente = clientes.idCliente
group by clientes.idCliente, clientes.nome;

insert into pedidos (idCliente, dataPedido, total)
values
(1, '2025-05-01', 100.00);

select 
    clientes.nome "Nome do Cliente",
    COUNT(pedidos.idPedido) "Total de Pedidos"
from clientes
join pedidos on pedidos.idCliente = clientes.idCliente
group by clientes.idCliente, clientes.nome;







