from flask import Flask, jsonify, request

app = Flask(__name__)

agents = {
    'ceo': {'role': 'CEO', 'resp': ['全局决策', '激励方向终审', '目标定调']},
    'hermes': {'role': 'Hermes执行总裁', 'resp': ['团队调度', '任务流管控', '进度统筹']},
    'strategist': {'role': '战略顾问', 'resp': ['顶层设计', '目标定调', '画布原型']},
    'emotion_advisor': {'role': '情绪顾问', 'resp': ['情绪价值', '记忆中枢', '动机反馈']},
    'architect': {'role': '系统架构师', 'resp': ['CBHB架构', '画布底层', '多Agent通信']},
    'algorithm_engineer': {'role': '核心算法工程师', 'resp': ['激励算法', '难度匹配', '动机建模']},
    'engineering_director': {'role': '全栈工程总监', 'resp': ['前后端一体化', 'API网关', '部署流水线']},
    'ai_model_engineer': {'role': 'AI模型工程师', 'resp': ['模型选型', 'API集成', '性能优化']},
    'qa_security': {'role': '自动化测试工程师', 'resp': ['自动化测试', '代码审计', '质量把关']},
    'visualizer_3d': {'role': '3D场景可视化师', 'resp': ['3D场景', '目标可视化', '物理交互']},
    'design_ops': {'role': '张工设计', 'resp': ['任务拆解', '施工图纸', '目标分解']},
}

@app.route('/')
def index():
    return jsonify({'message': 'AI Team API', 'status': 'running', 'agents': len(agents)})

@app.route('/api', methods=['GET', 'POST'])
def api():
    data = request.get_json() or {}
    action = data.get('action', request.args.get('action', ''))
    agent_id = data.get('agent_id', request.args.get('agent_id', 'ceo'))

    if action == 'status':
        if agent_id in agents:
            return jsonify({
                'status': 'success',
                'data': {'agent_id': agent_id, 'role': agents[agent_id]['role'], 'state': 'active', 'responsibilities': agents[agent_id]['resp']},
                'message': '状态查询成功'
            })
        return jsonify({'status': 'error', 'message': 'Agent not found'})
    return jsonify({'status': 'error', 'message': 'Unknown action'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
