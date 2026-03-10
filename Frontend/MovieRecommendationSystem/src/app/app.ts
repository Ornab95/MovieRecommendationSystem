import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MovieSearchComponent } from './components/movie-search/movie-search.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, MovieSearchComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('MovieRecommendationSystem');
}
