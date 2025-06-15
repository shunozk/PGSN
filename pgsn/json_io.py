import json

# 仮のPGSNデータ（ノードとリンク）
pgsn_data = {
    "nodes": [
        {"id": "G1", "type": "Goal", "content": "システムは安全であるべき"},
        {"id": "S1", "type": "Strategy", "content": "安全設計ガイドに従う"},
        {"id": "A1", "type": "Argument", "content": "チェックリストで確認した"}
    ],
    "links": [
        {"from": "G1", "to": "S1"},
        {"from": "S1", "to": "A1"}
    ]
}

# 保存
with open("pgsn_sample.json", "w", encoding="utf-8") as f:
    json.dump(pgsn_data, f, indent=2, ensure_ascii=False)

# 読み込み
with open("pgsn_sample.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
