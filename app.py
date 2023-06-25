from flask import Flask, request,jsonify
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'Welcome message': 'This is an API Service Provider of IPL data'})


@app.route('/api/teams')
def overall_teams():
    teams = analysis.total_teams()
    return jsonify(teams)

@app.route('/api/bowlers')
def overall_bowlers():
    bowlers = analysis.total_bowlers()
    return jsonify(bowlers)

@app.route('/api/batsmans')
def overall_batsmans():
    batsmans = analysis.total_batsmans()
    return jsonify(batsmans)

@app.route('/api/seasonwise-teamplayers')
def seasonwise_players():
    try:
        team = request.args.get('team')
        year = int(request.args.get('season'))
        players = analysis.team_players_yearwise(team,year)
        return jsonify(players)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/teamwise-players')
def teamwise_players():
    try:
        team = request.args.get('team')
        players = analysis.teamwise_players_played(team)
        return jsonify(players)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/teamwise-winnings')
def teamwise_winnings_details():
    try:
        team = request.args.get('team')
        response = analysis.number_of_winnings(team)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/overall-winnings')
def overall_winnings_details():
    response = analysis.winning_details_all_team()
    return jsonify(response)

@app.route('/api/teamvsteam-winnings')
def winnings_details_teamvsteam():
    try:
        team1 = request.args.get('team1')
        team2 = request.args.get('team2')
        response = analysis.team_vs_team(team1,team2)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/bowler-record')
def bowler_record():
    try:
        bowler = request.args.get('bowler')
        response = analysis.bowler_record(bowler)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/batsman-record')
def batsman_record():
    try:    
        batsman = request.args.get('batsman')
        response = analysis.batsman_record(batsman)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/team-record')
def team_record():
    try:
        team = request.args.get('team')
        response = analysis.team_record(team)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})
    
    
@app.route('/api/top-bowlers')
def top_bowlers():
    try:
        year = int(request.args.get('season'))
        top_n = int(request.args.get('n'))
        response = analysis.top_bowler_yearwise(year,top_k=top_n)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})

@app.route('/api/top-batsmans')
def top_batsmans():
    try:
        year = int(request.args.get('season'))
        top_n = int(request.args.get('n'))
        response = analysis.top_batsman_yearwise(year,top_k=top_n)
        return jsonify(response)
    except:
        return jsonify({'Error message': 'Enter correct inputs'})


if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port='5000')