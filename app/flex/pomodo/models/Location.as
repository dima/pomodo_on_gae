package pomodo.models {
  import org.ruboss.collections.ModelsCollection;
  import org.ruboss.models.RubossModel;
  
  [Resource(name="locations")]
  [Bindable]
  public class Location extends RubossModel {
    public static const LABEL:String = "name";

    public var name:String = "";

    public var notes:String = "";

    [BelongsTo]
    public var user:User;

    [HasMany]
    public var tasks:ModelsCollection;
    
    public function Location() {
      super(LABEL);
    }
  }
}
