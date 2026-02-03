"""Pydantic schemas for Scouting Report API."""

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field


class GameType(str, Enum):
    LOL = "lol"
    VALORANT = "Valorant"


class ChampionAgentStats(BaseModel):
    """Stats for a champion or agent."""

    name: str
    games_played: int = 0
    wins: int = 0
    losses: int = 0
    win_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    average_kda: float = 0.0
    pick_rate: float = Field(default=0.0, ge=0.0, le=1.0)


class PlayerProfile(BaseModel):
    """Individual player analysis."""

    player_id: str
    player_name: str
    role: Optional[str] = None
    primary_picks: list[ChampionAgentStats] = Field(default_factory=list)
    playstyle: str = ""  # "aggressive", "passive", "adaptive"
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    tendencies: list[str] = Field(default_factory=list)
    threat_level: str = "medium"  # "high", "medium", "low"
    notes: list[str] = Field(default_factory=list)

    # Game-specific stats
    average_stats: dict[str, float] = Field(default_factory=dict)


class CompositionAnalysis(BaseModel):
    """Team composition analysis."""

    composition: list[str] = Field(default_factory=list)
    games_played: int = 0
    win_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    strategy_type: str = ""  # e.g., "teamfight", "split-push", "pick"
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    power_spikes: list[str] = Field(default_factory=list)
    counter_strategies: list[str] = Field(default_factory=list)

    # VALORANT-specific
    map: Optional[str] = None
    site_preferences: dict[str, float] = Field(default_factory=dict)


class MapStats(BaseModel):
    """Map-specific statistics for VALORANT."""

    played: int = 0
    win_rate: float = Field(default=0.0, ge=0.0, le=1.0)


class ObjectiveAnalysis(BaseModel):
    """Objective control analysis."""

    objective_type: str
    priority_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    success_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    average_timing: Optional[str] = None
    tendencies: list[str] = Field(default_factory=list)


class TeamProfile(BaseModel):
    """Complete team analysis."""

    team_id: str
    team_name: str
    overall_record: dict[str, int] = Field(default_factory=dict)  # wins, losses
    playstyle: str = ""
    identity: str = ""  # e.g., "early game focused", "scaling team"

    # Strategic tendencies
    draft_tendencies: list[str] = Field(default_factory=list)  # LoL
    map_preferences: dict[str, MapStats] = Field(default_factory=dict)  # VALORANT

    # Objective analysis
    objectives: list[ObjectiveAnalysis] = Field(default_factory=list)

    # Common patterns
    early_game_patterns: list[str] = Field(default_factory=list)
    mid_game_patterns: list[str] = Field(default_factory=list)
    late_game_patterns: list[str] = Field(default_factory=list)

    # VALORANT-specific
    attack_tendencies: list[str] = Field(default_factory=list)
    defense_tendencies: list[str] = Field(default_factory=list)
    economy_patterns: list[str] = Field(default_factory=list)

    # Overall assessment
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)


class StrategyRecommendation(BaseModel):
    """Counter-strategy recommendation."""

    title: str
    priority: str = "medium"  # "high", "medium", "low"
    category: str = ""  # "draft", "early_game", "teamfight", "macro"
    description: str
    execution_steps: list[str] = Field(default_factory=list)
    risks: list[str] = Field(default_factory=list)
    success_indicators: list[str] = Field(default_factory=list)


class ScoutingReportRequest(BaseModel):
    """Request for scouting report generation."""

    opponent_team_id: str
    num_recent_matches: int = Field(default=10, ge=1, le=50)
    game: GameType
    include_player_profiles: bool = True
    include_composition_analysis: bool = True
    focus_areas: list[str] = Field(default_factory=list)


class ScoutingReportResponse(BaseModel):
    """Complete scouting report."""

    report_id: str
    opponent_team: TeamProfile
    player_profiles: list[PlayerProfile] = Field(default_factory=list)
    compositions: list[CompositionAnalysis] = Field(default_factory=list)
    key_findings: list[str] = Field(default_factory=list)
    preparation_priorities: list[str] = Field(default_factory=list)
    executive_summary: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    matches_analyzed: int = 0


class CounterStrategyRequest(BaseModel):
    """Request for counter-strategy generation."""

    opponent_team_id: str
    our_team_id: str
    game: GameType
    num_opponent_matches: int = Field(default=10, ge=1, le=50)
    num_our_matches: int = Field(default=5, ge=1, le=20)
    specific_focus: list[str] = Field(default_factory=list)


class CounterStrategyResponse(BaseModel):
    """Counter-strategy recommendations."""

    opponent_team_id: str
    our_team_id: str
    recommendations: list[StrategyRecommendation] = Field(default_factory=list)
    win_conditions: list[str] = Field(default_factory=list)
    draft_recommendations: list[str] = Field(default_factory=list)  # LoL
    map_recommendations: list[str] = Field(default_factory=list)  # VALORANT
    key_matchups: list[dict] = Field(default_factory=list)
    summary: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)


# New schemas for additional endpoints

class TeamSearchResult(BaseModel):
    """Single team in search results."""

    team_id: str
    team_name: str
    name_shortened: Optional[str] = None
    logo_url: Optional[str] = None
    primary_color: Optional[str] = None


class TeamSearchResponse(BaseModel):
    """Response for team search."""

    query: str
    game: GameType
    results: list[TeamSearchResult] = Field(default_factory=list)
    total_count: int = 0


class ReportHistoryItem(BaseModel):
    """Single report in history."""

    report_id: str
    opponent_team_id: str
    opponent_team_name: str
    game: GameType
    matches_analyzed: int
    generated_at: datetime


class ReportHistoryResponse(BaseModel):
    """Response for report history."""

    reports: list[ReportHistoryItem] = Field(default_factory=list)
    total_count: int = 0


class TeamCompareRequest(BaseModel):
    """Request for team comparison report."""

    team_a_id: str
    team_b_id: str
    game: GameType
    num_matches: int = Field(default=10, ge=1, le=50)


class TeamCompareResponse(BaseModel):
    """Response for team comparison report."""

    team_a: TeamProfile
    team_b: TeamProfile
    comparison_summary: str
    advantage: Optional[str] = None
    key_differences: list[str] = Field(default_factory=list)
    matchup_prediction: Optional[str] = None
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class DetailedMapStats(BaseModel):
    """Detailed map statistics."""

    map_name: str
    games_played: int = 0
    wins: int = 0
    losses: int = 0
    win_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    attack_rounds_won: int = 0
    attack_rounds_total: int = 0
    attack_win_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    defense_rounds_won: int = 0
    defense_rounds_total: int = 0
    defense_win_rate: float = Field(default=0.0, ge=0.0, le=1.0)
    avg_rounds_per_game: float = 0.0


class MapStatsResponse(BaseModel):
    """Response for detailed map statistics."""

    team_id: str
    team_name: str
    maps: list[DetailedMapStats] = Field(default_factory=list)
    best_map: Optional[str] = None
    worst_map: Optional[str] = None
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class PlayerThreat(BaseModel):
    """Player threat assessment."""

    player_id: str
    player_name: str
    role: Optional[str] = None
    threat_level: str = "medium"  # "high", "medium", "low"
    threat_score: float = Field(default=0.5, ge=0.0, le=1.0)
    primary_agents: list[str] = Field(default_factory=list)
    avg_kda: float = 0.0
    games_analyzed: int = 0
    key_strengths: list[str] = Field(default_factory=list)
    exploitable_weaknesses: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


class ThreatRankingResponse(BaseModel):
    """Response for player threat ranking."""

    team_id: str
    team_name: str
    players: list[PlayerThreat] = Field(default_factory=list)
    top_threat: Optional[str] = None
    summary: str = ""
    generated_at: datetime = Field(default_factory=datetime.utcnow)
