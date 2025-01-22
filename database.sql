CREATE TABLE `Produk` (
  `no` INTEGER NOT NULL AUTO_INCREMENT,
  `id_produk` INTEGER NOT NULL,
  `nama_produk` VARCHAR(200),
  `kategori` VARCHAR(50),
  `harga` DECIMAL(12,2),
  `status` VARCHAR(50),
  PRIMARY KEY (`id`)
);

INSERT INTO `Produk` (`nama_produk`, `price`) VALUES ('Amoi F99b', 100.00);
INSERT INTO `Produk` (`nama_produk`, `price`) VALUES ('BenQ-Siemens C81', 90