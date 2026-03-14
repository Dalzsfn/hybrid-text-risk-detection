from sqlalchemy import text
from backend.database.connection import engine
from urllib.parse import unquote


def get_patterns():
    with engine.connect() as conn:
        query = text("""
            SELECT 
                pattern AS patron, 
                category AS categoria, 
                risk_level AS nivel_alerta, 
                suggestion AS sugerencia 
            FROM patterns
        """)
        result = conn.execute(query)
        return [dict(row) for row in result.mappings()]


def add_pattern(pattern, category, risk, suggestion):
    with engine.begin() as conn:
        query = text("""
            INSERT INTO patterns (pattern, category, risk_level, suggestion)
            VALUES (:pattern, :category, :risk, :suggestion)
        """)
        
        conn.execute(query, {
            "pattern": pattern, 
            "category": category, 
            "risk": risk, 
            "suggestion": suggestion
        })
        
        
def delete_pattern(patron: str):
    patron_decodificado = unquote(patron)
    
    with engine.begin() as conn:
        query = text("DELETE FROM patterns WHERE pattern = :p")
        result = conn.execute(query, {"p": patron_decodificado})
    return {"ok": True}  