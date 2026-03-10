import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MovieService, MovieRecommendationResponse } from '../../services/movie.service';

@Component({
    selector: 'app-movie-search',
    standalone: true,
    imports: [CommonModule, FormsModule],
    templateUrl: './movie-search.component.html'
})
export class MovieSearchComponent {
    searchQuery = '';
    loading = signal(false);
    errorMessage = signal<string | null>(null);
    recommendations = signal<string[]>([]);
    currentMovie = signal<string | null>(null);
    isDarkMode = signal(true);

    constructor(private movieService: MovieService) { }

    toggleTheme(): void {
        this.isDarkMode.update(v => !v);
    }

    searchMovie(): void {
        const query = this.searchQuery.trim();
        if (!query) return;

        this.loading.set(true);
        this.errorMessage.set(null);
        this.recommendations.set([]);
        this.currentMovie.set(null);

        this.movieService.getRecommendations(query).subscribe({
            next: (response: MovieRecommendationResponse) => {
                this.currentMovie.set(response.movie);
                this.recommendations.set(response.recommendations || []);
                this.loading.set(false);
            },
            error: (error: Error) => {
                this.errorMessage.set(error.message);
                this.loading.set(false);
            }
        });
    }
}
