-- 1. TABELA DE USUÁRIOS
CREATE TABLE IF NOT EXISTS auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    is_superuser BOOLEAN NOT NULL DEFAULT 0,
    is_staff BOOLEAN NOT NULL DEFAULT 0,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2. TABELA CAIXAS
CREATE TABLE IF NOT EXISTS oficina_caixa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    identificacao TEXT NOT NULL,
    dono_id INTEGER NOT NULL,
    FOREIGN KEY (dono_id) REFERENCES auth_user(id) ON DELETE CASCADE
);

-- 3. TABELA FERRAMENTAS
CREATE TABLE IF NOT EXISTS oficina_ferramenta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    caixa_id INTEGER NOT NULL,
    FOREIGN KEY (caixa_id) REFERENCES oficina_caixa(id) ON DELETE CASCADE
);

-- ------------------------------------------------------------------------------------------------

-- 3 Usuários
INSERT OR IGNORE INTO auth_user (id, username, email, password, is_superuser, is_staff) VALUES 
(1, 'admin', 'admin@gmail.com', 'pbkdf2_sha256$senha_hash_admin...', 1, 1),
(2, 'cliente', 'cliente@gmail.com', 'pbkdf2_sha256$senha_hash_cliente...', 0, 0),
(3, 'funcionario', 'func@gmail.com', 'pbkdf2_sha256$senha_hash_func...', 0, 0);

-- 3 Caixas
INSERT OR IGNORE INTO oficina_caixa (id, identificacao, dono_id) VALUES 
(1, 'Caixa de Elétrica Profissional', 1),
(2, 'Caixa de Hidráulica Básica', 1),
(3, 'Kit de Emergência Doméstica', 2);

-- 3 Ferramentas
INSERT OR IGNORE INTO oficina_ferramenta (id, nome, descricao, caixa_id) VALUES 
(1, 'Alicate Universal', 'Cabo isolado 1000V vermelho', 1),
(2, 'Chave Inglesa', 'Abertura 12 polegadas cromada', 2),
(3, 'Martelo de Unha', 'Cabo de madeira envernizado', 3);